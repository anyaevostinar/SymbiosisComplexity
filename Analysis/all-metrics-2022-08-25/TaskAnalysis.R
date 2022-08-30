library(ggplot2)
library(viridis)
library(reshape2)

pdf("Tasks.pdf")

full_data <- read.csv("munged_tasks.csv")
final_update <- subset(full_data, update == 500000 & vert != 0.2)
final_update[final_update$vert == "No symbiont", c("vert", "partner")] <- list("", "nosym")

tasks <- c("NOT", "NAND", "AND", "ORN", "OR", "ANDN", "NOR", "XOR", "EQU")
task_columns <- lapply(tasks, function(x) paste0("task_", x))
task_map <- tasks
names(task_map) <- task_columns

task_data <- melt(final_update, id.vars=c("update", "vert", "partner"), measure.vars=task_columns)
# Wrapped version
ggplot(data=task_data, aes(x=partner, y=value, color=partner)) +
	geom_boxplot(alpha=0.5, outlier.size=0.25) +
	labs(y="Task completions in the last 5000 timesteps", x=NULL) +
	theme(panel.background = element_rect(fill='white', colour='black')) +
	theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(), legend.position='top') +
	guides(fill="none", x='none') +
	scale_x_discrete(labels=c('nosym'='Host without symbiont', 'host'='Host with symbiont', 'symbiont'='Symbiont')) +
	scale_color_manual(name="", values=viridis(3), guide=guide_legend(direction='horizontal'), breaks=c("host", "nosym", "symbiont"), labels=c("Host with symbiont", "Host without symbiont", "Symbiont")) +
	# scale_y_continuous(trans='log10')
	facet_wrap(~variable, scales="free_y", labeller=labeller(variable=task_map))
# 1-plot version
ggplot(data=task_data, aes(x=variable, y=value, color=partner)) +
	geom_boxplot(alpha=0.5, outlier.size=0.25) +
    ylab("Task completions in the last 5000 timesteps") +
	xlab("Task") +
	theme(panel.background = element_rect(fill='white', colour='black')) +
	theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(), legend.position='top') +
	guides(fill="none") +
	scale_x_discrete(labels=task_map) +
	scale_color_manual(name="", values=viridis(3), guide=guide_legend(direction='horizontal'), breaks=c("host", "nosym", "symbiont"), labels=c("Host with symbiont", "Host without symbiont", "Symbiont")) +
	scale_y_continuous(trans='log10')
	# facet_wrap(~variable, scales="free", labeller=labeller(variable=task_map))
