#
# This is the server logic of a Shiny web application. You can run the
# application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#
library(palmerpenguins)
library(shiny)


# Define server logic required to draw a histogram
shinyServer(function(input, output) {
  
  penguins_nomissing <- na.omit(penguins) #donnees pingouins
  
  
  output$flipperPlot <- renderPlot({
    #limite des pingouins
    penguinsLimit <- subset(penguins_nomissing,flipper_length_mm >= input$xlim[1] & flipper_length_mm <= input$xlim[2])
    if (input$typeHistogramme == "densité"  ) labelY <- "Densité" else labelY <- "Nombre de pingouins"
    
    ggplot(subset(penguinsLimit,species %in% input$species), aes(x=flipper_length_mm,color = sex, fill = species))+
      geom_histogram(
        if(input$typeHistogramme == "densité") aes(y = after_stat(density)) else aes(),
        alpha=0.6,
        position = 'identity',
        bins = 30,
        binwidth = 3,
      )+
    ggtitle(label= "Longueur des ailes en fonction du sexe et de l'espèce")+
    labs(x="Longueur des ailes",y = labelY, fill="Espèces", color ="Sexe")
  })

  output$billPlot <- renderPlot({
    penguinsLimitBill <- subset(penguins_nomissing,bill_length_mm >= input$xlimB[1] & bill_length_mm <= input$xlimB[2])
    
    ggplot(subset(penguinsLimitBill,species %in% input$species),aes(x=bill_length_mm, y=bill_depth_mm, color=species))+
      geom_point(position="Identity")+
      geom_smooth(method='loess',formula = 'y ~ x')+
      ggtitle(label="Longueur du Bec en fonction de la profondeur du bec, du sexe et de l'espèce") +
      labs(x="Profondeur du bec",y="Longueur du bec",color="Espèces")
      
  })
  output$summaryofvariable <- renderPrint({
    if(input$typeHistogramme == "densité") x    <- faithful[, 2] else x    <- faithful[, 1]
    summary(x)
  })
  
  output$text <- renderText({
    paste("Résumé de l'histogramme : ")
  })

})
