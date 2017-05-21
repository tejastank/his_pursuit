class NewSalesOrderPanel extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            details: [],
        };
    }

    fetchCustomers() {
        $("#cust-phone").autocomplete({
            source: '/sales/customer/list/?format=json',
            minLength: 4
        });
    }

    getDetailRowCount(details) {
        if (details.length === 0)
            return 1;
            
        return details[details.length-1].no + 1;
    }
        
    addItem(e) {
        e.preventDefault();

        var isValid = $('#add-row-form').isValid(null, null, true);
        
        if (isValid === false) {
            return;
        }
                
        var newrow = {
            no: this.getDetailRowCount(this.state.details),
            details: $('#ar-type').val(), 
            quantity: $('#ar-quantity').val(), 
            price: $('#ar-price').val() 
        };
        
        this.setState({details: this.state.details.concat([newrow])});
    }
    
    saveOrder(e) {
        e.preventDefault();
        var isValid = $('#create-sales-order-form').isValid(null, null, true);
        
        if (isValid === false) {
            return;
        }
        
        // construct the json object
        var data = {
            cust_phone: $('#cust-phone').val(),
            details: this.state.details,
        };
        
        var request = require('superagent');
        
        request
            .post('/sales/create-post/')
            .send(JSON.stringify(data))
            .set('Content-Type', 'application/json')
            .set('X-CSRFToken', getCookie('csrftoken'))
            .end(function(err, res) {
               // redirect to sales order portal or somewhere else
            });
    }
    
    componentDidMount() {
        this.fetchCustomers();
    }
   
    render() {
        return (
            <div className="row">
                <div className="col-md-4">
                    <form id="create-sales-order-form">
                        <div className="form-inline">
                            <label for="cust-phone">Customer:</label>
                            <input className="form-control" id="cust-phone" type="text" data-validation="required" />
                        </div>
                        <SalesNewOrderDetailTable clist={this.state.details} ref={(c) => {this.detailTable = c;}} />
                        <button className="btn btn-primary" onClick={(e) => this.saveOrder(e)}>Save Order</button>
                    </form>
                    
                    <form id="add-row-form" className="section-box">
                        <div className="form-group">
                            <label for="ar-type">Add Item</label>
                            <select className="form-control" id="ar-type">
                                <option>Suit Jacket</option>
                                <option>Suit Jackets</option>
                            </select>
                        </div>
                        <div className="form-group">
                            <label for="ar-quantity">Quantity:</label>
                            <input className="form-control" id="ar-quantity" type="text" data-validation="required,number" />
                        </div>
                        <div className="form-group">
                            <label for="ar-price">Price:</label>
                            <div className="input-group">
                                <div className="input-group-addon">$</div>
                                <input className="form-control" id="ar-price" type="text" data-validation="required,number" data-validation-allowing="float,negative" />
                            </div>
                        </div>
                        <button className="btn btn-primary" onClick={(e) => this.addItem(e)}>Add Item</button>
                    </form>                    
                </div>
                <div className="col-md-8">
                    <h1>hiii</h1>
                </div>
            </div>
        )
    }
}

class SalesNewOrderDetailTable extends React.Component {
    constructor(props) {
        super(props);
        
        this.props.list = [];
    }
    
    addNewRow() {
        var r = {no: 1, details: 'hi', quantity: 15, price: 14.3 };
        this.props.list.push(<SalesNewOrderDetailRow row={r} />);
    }
    
    render() {
    
        var rows = [];
        this.props.clist.forEach(function(r) {
            rows.push(<SalesNewOrderDetailRow row={r} />);
        });
        
        return(
            <table className="table table-bordered">
                <thead>
                    <tr>
                        <th><input type='checkbox' /></th>
                        <th>#</th>
                        <th>Details</th>
                        <th>Quantity</th>
                        <th>Price</th>
                    </tr>
                </thead>
                <tbody>
                {rows}
                </tbody>
            </table>  
        );
    }
}

class SalesNewOrderDetailRow extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <tr>
                <td><input type='checkbox' /></td>
                <td>{this.props.row.no}</td>
                <td>{this.props.row.details}</td>
                <td>{this.props.row.quantity}</td>
                <td>{this.props.row.price}</td>
            </tr>
        );
    }

}
        
if (document.getElementById('new-sales-order')) {
    ReactDOM.render(
        <NewSalesOrderPanel />,
        document.getElementById('new-sales-order'));
}