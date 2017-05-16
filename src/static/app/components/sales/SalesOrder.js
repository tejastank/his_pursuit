class SalesOrderBase extends React.Component {
    constructor(props) {
        super(props);
        
        this.state = {
            order: {}
        };
    }
}

class SalesOrderMain extends SalesOrderBase {
    render() {
        return (
            <div>
                <h1>Main</h1>
                <input type="text" value={this.state.order.id} />
            </div>
        );
    }
}

class SalesOrderDetails extends SalesOrderBase {
    render() {
        return (
            <h1>Details</h1>
        )
    }
}

class SalesOrder extends React.Component {

    constructor(props) {
        super(props);
        
        this.id = $.url().param('id');
    }

    componentDidMount() {
        $.getJSON('/sales/rest/order/' + this.id + '/?format=json')
        .then((order) => {
           this.main.setState({order: order[0]});
           this.details.setState({order: order[0]}); 
        });
    }
    
    render() {
        return (
            <div>
                <SalesOrderMain ref={(c) => {this.main = c;}} />
                <SalesOrderDetails ref={(c) => {this.details = c;}} />
            </div>
        );
    }
}

if (document.getElementById('sales_order')) {
    ReactDOM.render(
        <SalesOrder />,
        document.getElementById('sales_order'));
}