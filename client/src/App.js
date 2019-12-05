import React , {Component} from 'react';
//import './App.css';

const backendIP = 'http://34.83.87.49:8081';

class App extends Component {

  state = {
    data: [],
    loaded: false
  }

  componentDidMount(){
    this.loaded = true;
    for(let i = 1 ; i <= 6; i ++){
      this.getProjectQuery(i);
      console.log(i);
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
    
    fetch(`${backendIP}/api/query/${id}`)
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
    fetch(backendIP + '/api/getData')
      .then((data) => data.json())
      .then((res) => this.setState({data: res.data}));
  }
}




export default App;
