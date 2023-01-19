
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

      # If Conséquences sur le prix et l'environnement is selected
      conditionalPanel(
        condition = "input.tabSelected == 'Conséquences sur prix et environnement'",
        h5(align="center","Choix de la répartition des différentes filières de production"),
        sliderInput("hydraulic","Hydraulique:",min = 0, max = 100,value = c(10)),
        sliderInput("nuclear","Nucléaire:",min = 0, max = 100,value = c(10)),
        sliderInput("wind","Eolien:",min = 0, max = 100,value = c(10)),
        sliderInput("solar","Photovolatique:",min = 0, max = 100,value = c(10)),
        sliderInput("gas","Gaz:",min = 0, max = 100,value = c(10)),
        sliderInput("coal","Charbon:",min = 0, max = 100,value = c(10)),
        sliderInput("oil","Fioul:",min = 0, max = 100,value = c(10)),
      ),

      # If Becs - Longeur is selected
      conditionalPanel(
        condition = "input.tabSelected == 'Production'",
        sliderInput("ylim","Longueurs de becs considérés (mm):",min = 30, max = 60,value = c(30,60)),
      ),

      # If Becs - Longeur is selected
      conditionalPanel(
        condition = "input.tabSelected == 'Consommation'",
        sliderInput("zlim","Profondeurs de becs considérés (mm):",min = 10, max = 30,value = c(10,30)),
      ),

      # If Masse is selected
      conditionalPanel(
        condition = "input.tabSelected == 'Lien entre production et consommation'",
        sliderInput("wlim","Masses considérés (g):",min = 2500, max = 7500,value = c(2500,7500)),
      ),

      # If Masse is selected
      conditionalPanel(
        condition = "input.tabSelected == 'Confrontation des prédictions'",
        sliderInput("wlim","Masses considérés (g):",min = 2500, max = 7500,value = c(2500,7500)),
      )
    ),

    # Main
    mainPanel(
      navbarPage("Menu",id = "tabSelected",

        # Display of graphics according to the selected menu
        navbarMenu("Fenetres",
          tabPanel("Conséquences sur prix et environnement", textOutput("prixEnvironnement"),),
          tabPanel("Production",  plotOutput("billPlot")),
          tabPanel("Comsommation",  plotOutput("bill2Plot")),
          tabPanel("Lien entre production et consommation",  plotOutput("massPlot")),
          tabPanel("Confrontation des prédictions",  
          column(6,
         imageOutput("rte"), textOutput("introduction"), imageOutput("mix"), textOutput("mix2030"), imageOutput("consommation"), textOutput("consommation2030")
  )),
        )
      )
    )

  )
))
