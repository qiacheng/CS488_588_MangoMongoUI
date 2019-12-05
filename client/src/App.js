import React , {Component} from 'react';
//import './App.css';

class App extends Component {

  state = {
    data: [],
    loaded: false
  }

  componentDidMount(){
    this.loaded = true;
    for(let i = 1 ; i <= 6; i ++){
      this.getProjectQuery(i);
    }
    
  }

  render(){
    return (
      <div className="App">
        <header className="App-header">
          Hello World
          
        </header>
        <body>
          
          Q1: {this.state.data.Q1} <br /> <br/>
          Q2: {this.state.data.Q2} <br /> <br/>
          Q3: {this.state.data.Q3} <br /> <br/>
          Q4: {this.state.data.Q4} <br /> <br/>
          Q5: {this.state.data.Q5} <br /> <br/>
          Q6: {this.state.data.Q6} <br /> <br/>
          

        </body>
      </div>
    );
  }
  
  getProjectQuery(id){
    
    fetch(`http://localhost:3001/api/query/${id}`)
    .then((data) => data.json())
    .then((res) => {
      var result = this.state.data;
      result[`Q${id}`] = res.data.scriptPrints;
      this.setState({data: result})
      //console.log(JSON.stringify(this.state.data[`Q${id}`]))
      console.log(result);
    })  
   
  }

  getDataFromDb(){
    fetch('http://localhost:3001/api/getData')
      .then((data) => data.json())
      .then((res) => this.setState({data: res.data}));
  }
}




export default App;
