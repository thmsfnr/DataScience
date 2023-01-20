#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)

# Define UI for application that draws a histogram
shinyUI(fluidPage(

    # Application title
    titlePanel("Diagrammes d'analyse des pingouins"),

  
    sidebarLayout(
        sidebarPanel(
          checkboxGroupInput(inputId = "species",
                             label = "Espèces sélectionnées:",
                             choices = c("Adelie" = "Adelie",
                                         "Chinstrap" = "Chinstrap",
                                         "Gentoo" = "Gentoo"),selected="Adelie"
                          ),
          conditionalPanel(
            condition = "input.tabselected == 'Ailes'",
            sliderInput("xlim",
                        "Longueurs d'ailes considérées (mm)K:",
                        min = 170, max = 240,
                        value = c(170, 240)
            ),
            radioButtons("typeHistogramme", "Choix du type de l'histogramme", 
                         choices = c("densité","effectif"),selected="densité"),
            
          ),
          conditionalPanel(
            condition = "input.tabselected == 'Bec'",
            sliderInput("xlimB",
                        "Dimensions du bec considérés (mm)K:",
                        min = 32.0, 
                        max = 59.9,
                        value = c(32.0, 59.9)
            ),
          ),
        ),
  
        # Show a plot of the generated distribution
        mainPanel(
          navbarPage("Représentation",
                     navbarMenu("Histogrammes",
                                tabPanel("Ailes", plotOutput("flipperPlot")),
                                "----",
                                "Régression",
                                tabPanel("Bec",  plotOutput("billPlot")
                                )
                     ), id="tabselected"
          
          ),
          conditionalPanel(
            condition = "input.tabselected == 'Ailes'",
            textOutput("text"),
            verbatimTextOutput("summaryofvariable"),
          ),

      )
    )
  )
)
