// var jsonfile;
// $.getJSON('user_timeline_viz.json').done(function (data) {
//   jsonfile = data;
//  });

function createRange(meaNumber){
  if(meaNumber.length == 1){
    return [parseInt(meaNumber),parseInt(meaNumber)];
  } else{
    fNum = parseInt(meaNumber[0]);
    lNum = parseInt(meaNumber[meaNumber.length-1]);
    return [fNum, lNum];
  }
}

function arraysEqual(arr1, arr2) {
  if(arr1.length !== arr2.length)
    return false;
    for(var i = arr1.length; i--;) {
      if(arr1[i] !== arr2[i])
      return false;
    }
    return true;
}

function findArray(value, obJ){
  var results;
  for(var i=0; i < (obJ["data"].length); i++){
    if(value == obJ["data"][i]["label"]){
      results = obJ["data"][i];
    } else{
      results = -1;
    }
  }
  return results;
}



function genData(data_json, group_label, var1){
  //console.log("vv", JSON.stringify(jsonF));
  console.log("got here");
  //console.log("title", title);
  var forVis =[];
  var x = 0;
  for(var key in data_json){
    var dataOut = {};
    dataOut["group"] = group_label + key;
    dataOut["data"] = [];
    var dataLabels = [];
    var dataTypes = {};

    var fromsongs = data_json[key];

    for(i = 0; i < fromsongs.length; i++){
      var the_song = fromsongs[i][var1];
      //console.log(the_song,dataLabels );
      var typee = fromsongs[i].typee;
      var mea = createRange(fromsongs[i].measures);
      if(dataLabels.indexOf(the_song) == -1){
        song_dict = {};
        song_dict_info = {};

        song_dict["label"] = the_song;

        song_dict_info["val"] = typee;
        song_dict_info["timeRange"] = mea;
        dataTypes[the_song] = [typee,mea];
        //console.log(dataTypes);

        song_dict["data"] = [song_dict_info];
        dataOut["data"].push(song_dict);
        dataLabels.push(the_song);
      } else{
        song_dict_info = {};
        song_dict_info["val"] = typee;
        song_dict_info["timeRange"] = mea;

        var ind = (dataOut["data"]).map(function(o) { return o.label; }).indexOf(the_song);
        if(ind != -1){
          //console.log(dataTypes[the_song][0], dataTypes[the_song][1])
          //if(dataTypes[the_song][0] == typee && arraysEqual(dataTypes[the_song][1], mea) == true){
            //console.log("duplicate entry");
          //} else{
            dataOut["data"][ind]["data"].push(song_dict_info);
          //}
        } else{
          console.log("not in list of dict");
        }
      }
    }
    x+=1;
    forVis.push(dataOut);
  }
  var strr = JSON.stringify(forVis, null, 2);
  //console.log(strr);

  return forVis;
}


// function genData_org(){
//   //console.log("vv", JSON.stringify(jsonF));
//   //console.log(fromsongs);
//   var forVis =[];
//   var x = 0;
//   for(var title in jsonfile){
//     var dataOut = {};
//     dataOut["group"] = title;
//     dataOut["data"] = [];
//     var dataLabels = [];
//     var dataTypes = {};
//
//     var fromsongs = jsonfile[title];
//
//     for(i = 0; i < fromsongs.length; i++){
//       var the_song = fromsongs[i].Song_From;
//       //console.log(the_song,dataLabels );
//       var typee = fromsongs[i].typee;
//       var mea = createRange(fromsongs[i].measures);
//       if(dataLabels.indexOf(the_song) == -1){
//         song_dict = {};
//         song_dict_info = {};
//
//         song_dict["label"] = the_song;
//
//         song_dict_info["val"] = typee;
//         song_dict_info["timeRange"] = mea;
//         dataTypes[the_song] = [typee,mea];
//         //console.log(dataTypes);
//
//         song_dict["data"] = [song_dict_info];
//         dataOut["data"].push(song_dict);
//         dataLabels.push(the_song);
//       } else{
//         song_dict_info = {};
//         song_dict_info["val"] = typee;
//         song_dict_info["timeRange"] = mea;
//
//         var ind = (dataOut["data"]).map(function(o) { return o.label; }).indexOf(the_song);
//         if(ind != -1){
//           //console.log(dataTypes[the_song][0], dataTypes[the_song][1])
//           //if(dataTypes[the_song][0] == typee && arraysEqual(dataTypes[the_song][1], mea) == true){
//             //console.log("duplicate entry");
//           //} else{
//             dataOut["data"][ind]["data"].push(song_dict_info);
//           //}
//         } else{
//           console.log("not in list of dict");
//         }
//       }
//     }
//     x+=1;
//     forVis.push(dataOut);
//   }
//   var strr = JSON.stringify(forVis, null, 2);
//   //console.log(strr);
//
//   return forVis;
// }
