// making a binary search tree

class Tree{
    constructor(){
        this.root = null;
    }

    toObject(){
        return this.root;
    }
    add(value){
        if(this.root===null){
            this.root = new Node(value);
            return;
        }

        let current = this.root;
        while(true){ // loop indefinitely until we hit a break condition
            if (current.value > value){
                // go left
                if (current.left){ // if a left child is present
                    current = current.left; // then move to left child
                }

                // if no left child we put new value in new node as new left child
                else{ 
                    current.left = new Node(value);
                    return;
                }
            }
            else{
                // go right (if we don't go left then we go right)

                // check and see if there is a right child node or not
                if(current.right){
                    current = current.right;
                }
                else{
                    current.right = new Node(value);
                    return;
                }                
            }
        }
    }
}

class Node{
    constructor(value, left = null, right = null){
        this.value = value;
        this.left  = left;
        this.right = right;
    }
}

let t1 = new Tree();
t1.add(20);
t1.add(30);
t1.add(10);
t1.add(15);
t1.add(5);
t1.add(13);
t1.add(11);

console.log(t1.toObject())
