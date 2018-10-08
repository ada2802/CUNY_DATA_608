#
# This is a Shiny web application. 
#    http://shiny.rstudio.com/
#

library(ggplot2)
library(dplyr)
library(shiny)
library(tidyr)
library(plotly)
library(RCurl)

dat <- read.csv(text=getURL("https://raw.githubusercontent.com/ada2802/CUNY_DATA_608/master/module3/data/cleaned-cdc-mortality-1999-2010-2.csv"))

# Define UI for application that draws a histogram
ui <- fluidPage(
   
   # Application title
   titlePanel("US Morality Rate 2009-2010"),
   
   # Sidebar with a slider input for number of bins 
   sidebarLayout(
     sidebarPanel(
       
       #Drop Down for Cause of Death
       p("Question 1:Particular causes across different States by Year"),
       selectInput('deathCauseQ1', 'Deseases', unique(dat$ICD.Chapter), selected='"Diseases of the circulatory system"'),
       selectInput('yearQ1', 'Year', unique(dat$Year), selected='2010'),
       br(),
       p("Question 2:Particular States VS National Rate (per cause)"),
       selectInput('deathCauseQ2', 'Deseases', unique(dat$ICD.Chapter), selected='"Diseases of the circulatory system"')
       
     ),
     
     # Show a plot of the generated distribution
     mainPanel(
       plotOutput("distPlotQ1"),
       plotOutput("distPlotQ2")
      )
   )
)

# Define server logic required to draw a histogram
server <- function(input, output) {
  
  output$distPlotQ1 <- renderPlot({
    
    by_cause_of_death_data <- dat %>%
      filter(ICD.Chapter == input$deathCauseQ1 & dat$Year == input$yearQ1) %>%
      arrange(desc(Crude.Rate))
    
    by_cause_of_death_data$Crude.Rate.Rank <- rank(by_cause_of_death_data$Crude.Rate)
    
    
    #display: even only one row of data per industry, use sum and display the values
    p <- ggplot(by_cause_of_death_data, aes(x=reorder(State, Crude.Rate.Rank),y=Crude.Rate.Rank,fill=State)) + 
      geom_bar(stat = "identity") + ggtitle(paste("Q1:", input$deathCauseQ1, " by year ", input$yearQ1 ))
    
    #output as "return"
    p + coord_flip()
    
  })
  
  output$distPlotQ2 <- renderPlot({
    
    State_Crude.Rate <- dat %>%
      filter(ICD.Chapter == input$deathCauseQ2) %>%
      select(Year, State, Crude.Rate)
    
    
    
    National_Crude.Rate <-  dat %>%
      filter(ICD.Chapter == input$deathCauseQ2) %>%
      group_by(Year) %>%
      summarize(Nation_death = sum(Deaths, na.rm = TRUE),Nation_popul = sum(Population, na.rm = TRUE))  %>%
      mutate(Crude.Rate = Nation_death/Nation_popul*100000)%>%
      mutate(State = "Nation")%>%
      select(Year,State,Crude.Rate)
    
    Nation_State_Crude.Rate <- rbind(National_Crude.Rate,State_Crude.Rate)
    
    
    
    #display: even only one row of data per industry, use sum and display the values
    p <- ggplot(Nation_State_Crude.Rate, aes(x=Year,y=Crude.Rate, group = State)) + 
      
      geom_line(aes(linetype=State,color=State))+
      geom_point(aes(shape=State,color=State)) +
      
      ggtitle(paste("Q2:", input$deathCauseQ2, " by year" ))
    
    #output as "return"
    p 
    
    
  })
  
  
  
  
}

# Run the application 
shinyApp(ui = ui, server = server)

