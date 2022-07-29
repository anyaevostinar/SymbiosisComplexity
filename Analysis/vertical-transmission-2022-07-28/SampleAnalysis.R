require(ggplot2)
library(viridis)

#Set your working directory to the Analysis folder for your project

#Read in the data
initial_data <- read.csv("munged_tasks.csv", h=T)
final_update <- subset(initial_data, update == "50000")

plot <- function(name, task) {
    #Plot the host and symbiont interaction values by vertical transmission rate
    ggplot(data=final_update, aes(x=factor(as.character(vert), levels=unique(vert)), y={{ name }}, color=partner)) +
    	geom_boxplot(alpha=0.5, outlier.size=0, orientation="x") +
        ylab(paste("Completions of ", task, " in the last 5000 timesteps")) +
    	xlab("Vertical transmission rate") +
    	theme(panel.background = element_rect(fill='white', colour='black')) +
    	theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank()) +
    	guides(fill=FALSE)
    	#ylim(0,400000) +
    	#scale_color_manual(name="", values=viridis(2))
    	#facet_wrap(~inflow)
}

plot(task_NOT, "NOT")
plot(task_NAND, "NAND")
plot(task_AND, "AND")
plot(task_ORN, "ORN")
plot(task_OR, "OR")
plot(task_ANDN, "ANDN")
plot(task_NOR, "NOR")
plot(task_XOR, "XOR")
plot(task_EQU, "EQU")


ggplot(data=subset(final_update, partner == "symbiont"), aes(x=factor(as.character(vert), levels=unique(vert)), y=donated)) +
	geom_boxplot(alpha=0.5, outlier.size=0, orientation="x") +
    ylab("Proportion of symbiont resources donated") +
	xlab("Vertical transmission rate") +
	theme(panel.background = element_rect(fill='white', colour='black')) +
	theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank()) +
	guides(fill=FALSE)
	#ylim(0,400000) +
	#scale_color_manual(name="", values=viridis(2))
	#facet_wrap(~inflow)
