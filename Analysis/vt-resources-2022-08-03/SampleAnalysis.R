library(ggplot2)
library(viridis)
library(reshape2)
library(gridExtra)

#Set your working directory to the Analysis folder for your project

#Read in the data
initial_data <- read.csv("munged_tasks.csv", h=T)
final_update <- subset(initial_data, update == "50000")
final_update[final_update$vres == "No symbiont", c("vres", "partner")] <- list("", "nosym")

tasks <- c("NOT", "NAND", "AND", "ORN", "OR", "ANDN", "NOR", "XOR", "EQU")
task_columns <- lapply(tasks, function(x) paste0("task_", x))
task_map <- tasks
names(task_map) <- task_columns

task_data <- melt(final_update, id.vars=c("update", "vres", "partner"), measure.vars=task_columns)
ggplot(data=task_data, aes(x=factor(as.character(vres), levels=unique(vres)), y=value, color=partner)) +
	geom_boxplot(alpha=0.5, outlier.size=0.25) +
    ylab("Task completions in the last 5000 timesteps") +
	xlab("Vertical transmission resources") +
	theme(panel.background = element_rect(fill='white', colour='black')) +
	theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(), legend.position='top') +
	guides(fill="none") +
	scale_color_manual(name="", values=viridis(3), guide=guide_legend(direction='horizontal'), breaks=c("nosym", "host", "symbiont"), labels=c("Host without symbiont", "Host with symbiont", "Symbiont")) +
	# scale_y_continuous(trans='log10') +
	facet_wrap(~variable, scales="free", labeller=labeller(variable=task_map))

donated_data <- melt(subset(final_update, partner=="symbiont"), id.vars=c("vres"), measure.vars=c("earned", "donated"))
a <- ggplot(data=donated_data, aes(x=factor(as.character(vres), levels=unique(vres)), y=value, color=variable)) +
	geom_boxplot(alpha=0.5, outlier.size=0.5) +
    ylab("Total symbiont resources earned and donated") +
	xlab("Vertical transmission resources") +
	theme(panel.background = element_rect(fill='white', colour='black')) +
	theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(), legend.position='top') +
	guides(fill="none") +
	scale_color_manual(name="", values=viridis(2), guide=guide_legend(direction='horizontal'), breaks=c("earned", "donated"), labels=c("Symbiont earned resources", "Symbiont donated resources"))
b <- ggplot(data=subset(final_update, partner=="symbiont"), aes(x=factor(as.character(vres), levels=unique(vres)), y=donate_calls)) +
	geom_boxplot(alpha=0.5, outlier.size=0.5) +
    ylab("Total times symbionts ran the donate instruction in the last 5000 timesteps") +
	xlab("Vertical transmission resources") +
	theme(panel.background = element_rect(fill='white', colour='black')) +
	theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(), legend.position='top') +
	guides(fill="none")# +
	#scale_color_manual(name="", values=viridis(2), guide=guide_legend(direction='horizontal'), breaks=c("earned", "donated"), labels=c("Symbiont earned resources", "Symbiont donated resources"))
grid.arrange(a, b, ncol=2, nrow=1)
