
# Thomas Fournier

library(shiny)

# Define UI for the application
shinyUI(fluidPage(

  # Application header
  titlePanel(h2(align="center","Energie en France")),
  fluidRow(h4(align="center","Ce projet est une analyse de la sortie du nucléaire dans la production d'électricité française réalisée lors d'un cours à Polytech Montpellier.")),
  fluidRow(h3("")),

  sidebarLayout(

    # Sidebar
    sidebarPanel(

      p("Ce projet visait initialement à nous permettre d'approfondir certaines connaissances acquises au cours de notre formation, d'en découvrir d'autres, d'identifier des méthodes appropriées pour répondre à un objectif donné, de combiner des méthodes complémentaires, de comparer des méthodes concurrentes pour répondre à des objectifs donnés, d'interpréter et éventuellement de comparer les résultats des méthodes mises en œuvre, ainsi que d'avoir un esprit critique vis-à-vis de la collecte des données, des méthodes mises en œuvre et de leur paramétrage."),
      p("Concernant le sujet, nous avions le choix entre différents thèmes et nous avons choisi celui lié à l'étude des données ouvertes, plus précisément lié au projet d'Université des données ouvertes mené par l'association Latitudes en lien avec le site institutionnel national data gouv. Les jeux de données de ce thème sont alors multiples, sachant que nous avons fait le choix d'étudier celui associé à l'énergie en France."),
      p("Concernant la problématique, nous en avons choisi une qui diffère de celle proposée dans le projet. Au lieu de centrer notre étude sur les conséquences énergétiques de la guerre en Ukraine, nous allons déterminer les conséquences de la fin du nucléaire dans la production d'électricité en France."),
      a(href = "https://github.com/thmsfnr/DataScience", "Cliquez ici pour plus d'informations"),
      tags$hr(style = "border:1px solid black;"),
      p("Il est possible de choisir entre l'affichage de la répartition des espèces ou des sexes selon la caractéristique sélectionnée."),
      radioButtons("varChoice","Elément souhaité :",choices = c("Espèce", "Sexe"),selected = "Espèce"),

      # If Espèce is selected
      conditionalPanel(
        condition = "input.varChoice == 'Espèce'",
        checkboxGroupInput(inputId = "species", label = "Espèces sélectionnées:",choices = c("Adelie" = "Adelie","Chinstrap" = "Chinstrap","Gentoo" = "Gentoo"),selected=c("Adelie","Chinstrap","Gentoo"))
      ),

      # If Ailes is selected
      conditionalPanel(
        condition = "input.tabSelected == 'Ailes'",
        sliderInput("xlim","Longueurs d'ailes considérées (mm):",min = 170, max = 240,value = c(170,240)),
      ),

      # If Becs - Longeur is selected
      conditionalPanel(
        condition = "input.tabSelected == 'Becs - Longeur'",
        sliderInput("ylim","Longueurs de becs considérés (mm):",min = 30, max = 60,value = c(30,60)),
      ),

      # If Becs - Longeur is selected
      conditionalPanel(
        condition = "input.tabSelected == 'Becs - Profondeur'",
        sliderInput("zlim","Profondeurs de becs considérés (mm):",min = 10, max = 30,value = c(10,30)),
      ),

      # If Masse is selected
      conditionalPanel(
        condition = "input.tabSelected == 'Masses'",
        sliderInput("wlim","Masses considérés (g):",min = 2500, max = 7500,value = c(2500,7500)),
      )
    ),

    # Main
    mainPanel(
      navbarPage("Menu",id = "tabSelected",

        # Display of graphics according to the selected menu
        navbarMenu("Caractéristiques",
          tabPanel("Ailes", plotOutput("fliperPlot")),
          tabPanel("Becs - Longeur",  plotOutput("billPlot")),
          tabPanel("Becs - Profondeur",  plotOutput("bill2Plot")),
          tabPanel("Masses",  plotOutput("massPlot")),
          tabPanel("Iles",  plotOutput("islandPlot")),
        )
      )
    )

  )
))
