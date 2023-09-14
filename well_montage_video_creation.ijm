#@ String(value="Please select the folder containing the files you wish to combine.", visibility="MESSAGE") message
#@ File(style="directory") inputFolder
#@ File(style="directory") outputFolder
#@ Integer(label="Number of time points in time series") last_time_point
#@ Integer(label="Number of columns of final montage") montage_columns
#@ Integer(label="Number of rows of final montage") montage_rows
#@ Integer(label="Montage width (px)") montage_width
#@ Integer(label="Frame rate for final video (fps)") frame_rate
#@ String(label="Video output name", value="Multiwell-montage") video_file_name

setBatchMode("hide");
interval = 1/frame_rate * 1000; 


for (i = 1; i < (last_time_point + 1); i++) {
	if (i< 10) {
		time_point = "t0" + i;
	}
	else {
		time_point = "t" + i;
	}
	File.openSequence(inputFolder, " filter=" + time_point);
	run("Make Montage...", "columns=" + montage_columns + " rows=" + montage_rows + " scale=1 border=10");
	saveAs("PNG", outputFolder + File.separator + "Montage_" + time_point + ".png");
	close("*");
}

File.openSequence(outputFolder, " filter=Montage"); 
//run("Images to Stack", "use");
run("Size...", "width="+ montage_width + " constrain average interpolation=Bilinear");
run("Animated Gif ... ", "name=Stack set_global_lookup_table_options=[Load from Current Image] optional=[] image=[No Disposal] set="+ interval + " number=0 transparency=[No Transparency] red=0 green=0 blue=0 index=0 filename=[" + outputFolder + File.separator + video_file_name +".gif]");
close();

setBatchMode("show");

beep(); 
showMessage("Done!");