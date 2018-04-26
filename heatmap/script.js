// var jsonfile;
// $.getJSON('user_timeline_viz.json').done(function (data) {
//   jsonfile = data;
//  });

/*
  GOAL: var1 and the_session are defined outside genData and passed as parameters so we can switch
 between json Visualizations

 */

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

function get_relSongs(data_json, title, attr_y){
  var relsongs = [];
  for( var x in data_json[title]){
    var the_song = data_json[title][x][attr_y];
    if(relsongs.indexOf(the_song) == -1){
      relsongs.push(the_song);
    }
  }
  return relsongs;
}




function genData(data_json, title, attr_y, attr_z, color_by){
  // console.log("coloring by ", color_by);
  //console.log("vv", JSON.stringify(jsonF));
  //console.log("got here");
  //console.log("title", title);
  var forVis =[];
  var x = 0;

  var relSongs = get_relSongs(data_json, title, attr_y);
  //console.log(relSongs);

  for(var x in relSongs){
    var the_song = relSongs[x];
    var dataOut = {};
    dataOut["group"] = the_song;
    dataOut["data"] = [];
    var dataLabels = [];
    var dataTypes = {};



    var fromsongs = data_json[title];
    //console.log(fromsongs);

    for(i = 0; i < fromsongs.length; i++){
      var mea;
      var get_type;
      var the_session = fromsongs[i][attr_z];
      var _song = fromsongs[i][attr_y];

      var typee = fromsongs[i][color_by];
      //var typee = fromsongs[i].typee;
      //var typee = fromsongs[i].get_type;
      //var mea = createRange(fromsongs[i].measures);
      var meaNum = (fromsongs[i].measures).split(",")

      for(x = 0; x < meaNum.length; x++) {

      var _rmeaNum = meaNum[x].split("-")
      //console.log("meaNum: ", meaNum[x]);
      //console.log("_rmeaNum: ", _rmeaNum);
      if(_rmeaNum.length == 1){
        mea = [parseInt(_rmeaNum[0]),parseInt(_rmeaNum[0])]
      } else{
        mea = [parseInt(_rmeaNum[0]),parseInt(_rmeaNum[1])]
      }

      //console.log("the original measure numbers: ", fromsongs[i].measures, "the new mea: ", mea);

      if((dataLabels.indexOf(the_session) == -1 )&& (_song == the_song)){
        song_dict = {};
        song_dict_info = {};

        song_dict["label"] = the_session;

        song_dict_info["val"] = typee;
        song_dict_info["timeRange"] = mea;
        dataTypes[the_session] = [typee,mea];
        //console.log(dataTypes);

        song_dict["data"] = [song_dict_info];
        dataOut["data"].push(song_dict);
        dataLabels.push(the_session);
        //console.log(dataLabels);
        //console.log(dataOut["data"]);
        //Sermisy, Claudin de : Sermisy. Missa Tota pulchra es (Credo)
      } else{
        song_dict_info = {};
        song_dict_info["val"] = typee;
        song_dict_info["timeRange"] = mea;
        //console.log("here");
        var ind = (dataOut["data"]).map(function(o) { return o.label; }).indexOf(the_session);
        //console.log("the ind: ", ind);
        if(ind != -1){
          //console.log(dataTypes[the_song][0], dataTypes[the_song][1])
          //if(dataTypes[the_song][0] == typee && arraysEqual(dataTypes[the_song][1], mea) == true){
            //console.log("duplicate entry");
          //} else{
            dataOut["data"][ind]["data"].push(song_dict_info);
          //}
        } else{
          //console.log("not in list of dict");
        }
      }
    }// end meaNum.length for loop
    } // end fromsongs.length for loop
    x+=1;
    forVis.push(dataOut);
  }
  var strr = JSON.stringify(forVis, null, 2);
  //console.log("The data :" , strr);

  return forVis;
}


// function genData(data_json, title, group_label, var1){
//   //console.log("vv", JSON.stringify(jsonF));
//   //console.log("got here");
//   //console.log("title", title);
//   var forVis =[];
//   var x = 0;
//
//   var relSongs = get_relSongs(data_json, title, var1);
//   //console.log(relSongs);
//
//   //for(var the_song in relSongs){
//     //console.log("key", key);
//     var dataOut = {};
//     dataOut["group"] = group_label + the_song;
//     dataOut["data"] = [];
//     var dataLabels = [];
//     var dataTypes = {};
//
//     var fromsongs = data_json[title];
//     console.log(fromsongs);
//
//     for(i = 0; i < fromsongs.length; i++){
//       var the_song = fromsongs[i][var1];
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
//   //}
//   var strr = JSON.stringify(forVis, null, 2);
//   //console.log(strr);
//
//   return forVis;
// }

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
