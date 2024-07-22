from flask import request, jsonify
from app import app, db
from app.models import Parent, Child, Blog

@app.route('/parents', methods=['POST'])
def create_parent():
    data = request.get_json()
    new_parent = Parent(
        name=data['name'],
        email=data['email'],
        parent_type=data['parent_type'],
        location=data.get('location'),
        interest=data.get('interest') 
    )
    db.session.add(new_parent)
    db.session.commit()
    return jsonify({'message': 'Parent created successfully'}), 201

@app.route('/parents/<int:id>', methods=['GET'])
def get_parent(id):
    parent = Parent.query.get_or_404(id)
    return jsonify({
        'id': parent.id,
        'name': parent.name,
        'email': parent.email,
        'parent_type': parent.parent_type,
        'location': parent.location,   # Added
        'interest': parent.interest    # Added
    })

@app.route('/parents/<int:id>', methods=['PUT'])
def update_parent(id):
    data = request.get_json()
    parent = Parent.query.get_or_404(id)
    parent.name = data.get('name', parent.name)
    parent.email = data.get('email', parent.email)
    parent.parent_type = data.get('parent_type', parent.parent_type)
    parent.location = data.get('location', parent.location)  # Optional
    parent.interest = data.get('interest', parent.interest)   # Optional
    db.session.commit()
    return jsonify({'message': 'Parent updated successfully'})

@app.route('/parents/<int:id>', methods=['DELETE'])
def delete_parent(id):
    parent = Parent.query.get_or_404(id)
    db.session.delete(parent)
    db.session.commit()
    return jsonify({'message': 'Parent deleted successfully'})

@app.route('/home_feed/<int:parent_id>', methods=['GET'])
def home_feed(parent_id):
    parent = Parent.query.get_or_404(parent_id)
    child = Child.query.filter_by(parent_id=parent_id).first()
    
    if not child:
        return jsonify({'message': 'Child not found for this parent'}), 404

    blogs = Blog.query.all() 
    
    feed = [{
        'title': blog.title,
        'content': blog.content,
        'author': blog.author,
        'publication_date': blog.publication_date
    } for blog in blogs]
    
    return jsonify({'home_feed': feed})


@app.route('/parents_by_interest/<string:interest>', methods=['GET'])
def get_parents_by_interest(interest):
    parents = Parent.query.filter_by(interest=interest).all()
    
    if not parents:
        return jsonify({'message': 'No parents found with this interest'}), 404

    result = []
    
    for parent in parents:
        children = Child.query.filter_by(parent_id=parent.id).all()
        
        children_data = [{
            'id': child.id,
            'name': child.name,
            'age': child.age,
            'gender': child.gender
        } for child in children]
        
        result.append({
            'parent': {
                'id': parent.id,
                'name': parent.name,
                'email': parent.email,
                'parent_type': parent.parent_type,
                'location': parent.location,
                'interest': parent.interest
            },
            'children': children_data
        })
    
    return jsonify(result)

