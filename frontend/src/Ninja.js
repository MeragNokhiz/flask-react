import React, { Component } from 'react';


class Ninja extends Component {

    constructor(props) {
        super(props);
        this.state = { record: [], };
    }

    componentDidMount() {
        const API = 'https://s3.eu-central-1.amazonaws.com/jobninja-backend-feeds-prod/b59cfa0a-6f55-44ab-b700-901173f9d29d/jobs_feed.xml';
        fetch(API)
            .then(response => response.text())
            .then(data => console.log(data))
            .catch(err => console.log("--> Error: " +err));
    }

    render() {

        const { record } = this.state;
        return (
            <ul>
            {record.map(record =>
                <li key={record.objectID}>
                <a href={record.url}>{record.title}</a>
                </li>
            )}
            </ul>
        );
    }
}

export default Ninja;