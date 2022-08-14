library(ggplot2)
library(viridis)
library(reshape2)
library(gridExtra)

pdf("OverTime.pdf")

#Set your working directory to the Analysis folder for your project

#Read in the data
initial_data <- read.csv("munged_tasks.csv", h=T)
#initial_data[initial_data$vert == "No symbiont", c("vert", "partner")] <- list("", "nosym")

tasks <- c("NOT", "NAND", "AND", "ORN", "OR", "ANDN", "NOR", "XOR", "EQU")
task_columns <- lapply(tasks, function(x) paste0("task_", x))
task_map <- tasks
names(task_map) <- task_columns

vt_label = function(l) {
    l$vert <- lapply(l$vert, function(x) paste(if (x == "No symbiont") { "" } else { "Vertical transmission" }, x))
    l
}

task_data <- melt(initial_data, id.vars=c("update", "vert", "partner"), measure.vars=task_columns)
for (t in task_columns) {
    print(ggplot(data=subset(task_data, variable==t), aes(x=update, y=value, color=partner, fill=partner)) +
        stat_summary(fun.data="mean_se", geom=c("smooth"), se=TRUE) +
        ylab("Task completions") +
    	xlab("Update") +
    	ggtitle(paste("Completions of task", task_map[t])) +
    	theme(panel.background = element_rect(fill='white', colour='black')) +
    	theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(), legend.position='top', plot.title=element_text(hjust=0.5)) +
    	guides(fill="none") +
    	scale_color_manual(name="", values=viridis(2), guide=guide_legend(direction='horizontal'), breaks=c("host", "symbiont"), labels=c("Host", "Symbiont")) +
        scale_fill_manual(values=viridis(2), breaks=c("host", "symbiont")) +
    	#scale_y_continuous(trans='log10') +
    	facet_wrap(~vert, labeller=vt_label)
    	)
}

donated_data <- melt(subset(initial_data, partner=="symbiont"), id.vars=c("update","vert"), measure.vars=c("earned", "donated"))
ggplot(data=donated_data, aes(x=update, y=value, color=variable, fill=variable)) +
    stat_summary(fun.data="mean_se", geom=c("smooth"), se=TRUE) +
    ylab("Total resources") +
    ggtitle("Symbiont resources earned and donated") +
	xlab("Update") +
	theme(panel.background = element_rect(fill='white', colour='black')) +
	theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(), legend.position='top', plot.title=element_text(hjust=0.5)) +
	guides(fill="none") +
	scale_color_manual(name="", values=viridis(2), guide=guide_legend(direction='horizontal'), breaks=c("earned", "donated"), labels=c("Symbiont earned resources", "Symbiont donated resources")) +
    scale_fill_manual(values=viridis(2), breaks=c("earned", "donated")) +
    facet_wrap(~vert, labeller=vt_label)
ggplot(data=subset(initial_data, partner=="symbiont"), aes(x=update, y=donate_calls)) +
    stat_summary(fun.data="mean_se", geom=c("smooth"), se=TRUE) +
    ggtitle("Total times symbionts ran the donate instruction") +
    ylab("Times donated") +
	xlab("Update") +
	theme(panel.background = element_rect(fill='white', colour='black')) +
	theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(), legend.position='top', plot.title=element_text(hjust=0.5)) +
	guides(fill="none") +
    facet_wrap(~vert, labeller=vt_label)
ggplot(data=subset(initial_data, partner=="symbiont" & is.finite(mutualism)), aes(x=factor(as.character(vert), levels=unique(vert)), y=mutualism)) +
	geom_boxplot(alpha=0.5, outlier.size=0.5) +
    ggtitle("Average mutualism in the dominant host") +
    ylab("Mutualism") +
    ylim(-1, 1) +
	xlab("Vertical transmission rate") +
	theme(panel.background = element_rect(fill='white', colour='black')) +
	theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(), legend.position='top', plot.title=element_text(hjust=0.5)) +
	guides(fill="none")# +
	#scale_color_manual(name="", values=viridis(2), guide=guide_legend(direction='horizontal'), breaks=c("earned", "donated"), labels=c("Symbiont earned resources", "Symbiont donated resources"))
#grid.arrange(a, arrangeGrob(b, c, ncol=2), nrow=2 )

trans_data <- melt(subset(initial_data, partner=="symbiont"), id.vars=c("update","vert"), measure.vars=c("attempts_horiz", "success_horiz", "attempts_vert"))
ggplot(data=trans_data, aes(x=update, y=value, color=variable, fill=variable)) +
    stat_summary(fun.data="mean_se", geom=c("smooth"), se=TRUE) +
    ylab("Transmission events") +
    ggtitle("Symbiont transmission events") +
	xlab("Update") +
	theme(panel.background = element_rect(fill='white', colour='black')) +
	theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(), legend.position='top', plot.title=element_text(hjust=0.5)) +
	guides(fill="none") +
	scale_color_manual(name="", values=viridis(3), guide=guide_legend(direction='horizontal'), breaks=c("attempts_horiz", "success_horiz", "attempts_vert"),
		labels=c("Attempted horizontal transmission", "Successful horizontal transmission", "Vertical transmission")) +
    scale_fill_manual(values=viridis(3), breaks=c("attempts_horiz", "success_horiz", "attempts_vert")) +
    facet_wrap(~vert, labeller=vt_label)
trans_data <- melt(subset(initial_data, partner=="symbiont"), id.vars=c("update","vert"), measure.vars=c("success_horiz", "attempts_vert"))
ggplot(data=trans_data, aes(x=update, y=value, color=variable, fill=variable)) +
    stat_summary(fun.data="mean_se", geom=c("smooth"), se=TRUE) +
    ylab("Transmission events") +
    ggtitle("Symbiont transmission events") +
	xlab("Update") +
	theme(panel.background = element_rect(fill='white', colour='black')) +
	theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(), legend.position='top', plot.title=element_text(hjust=0.5)) +
	guides(fill="none") +
	scale_color_manual(name="", values=viridis(2), guide=guide_legend(direction='horizontal'), breaks=c("success_horiz", "attempts_vert"),
		labels=c("Successful horizontal transmission", "Vertical transmission")) +
    scale_fill_manual(values=viridis(2), breaks=c("success_horiz", "attempts_vert")) +
    facet_wrap(~vert, labeller=vt_label)

warnings()
