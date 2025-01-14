import copy

class SelfReferencingEntity:
    def __init__(self):
        self.parent = None
        
    def set_parent(self, parent):
        self.parent = parent
        
class SomeComponent:
    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref
    
    def __copy__(self):
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__.update(self.__dict__)

        return new
    
    def __deepcopy__(self, memo=None):
        if memo is None:
            memo = {}
        
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)
        
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        
        new.__dict__ = copy.deepcopy(self.__dict__, memo)
        
        return new

if __name__ == "__main__":
    
    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    component = SomeComponent(23, list_of_objects, circular_ref)
    circular_ref.set_parent(component)
    
    shallow_copied_component = copy.copy(component)
    
    shallow_copied_component.some_list_of_objects.append("another object")
    
    component.some_list_of_objects[1].add(4)
    print(" --- check original and copy (shallow copy) ---")
    print(component.some_list_of_objects)
    print(shallow_copied_component.some_list_of_objects)

    deep_copied_component = copy.deepcopy(component)
    deep_copied_component.some_list_of_objects.append("one more object")
    component.some_list_of_objects[1].add(10)
    print(" --- check original and copy (deep copy) ---")
    print(component.some_list_of_objects)
    print(deep_copied_component.some_list_of_objects)
    
    
    print(
        f"id(deep_copied_component.some_circular_ref.parent): "
        f"{id(deep_copied_component.some_circular_ref.parent)}"
    )
    print(
        f"id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent): "
        f"{id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent)}"
    )
    print(
        "^^ This shows that deepcopied objects contain same reference, they are not cloned repeatedly."
    )
    print(
        f"circular address check: "
        f"{id(component.some_circular_ref)} / {id(deep_copied_component.some_circular_ref)}"
    )
    
## output
"""
 --- check original and copy (shallow copy) ---
[1, {1, 2, 3, 4}, [1, 2, 3], 'another object']
[1, {1, 2, 3, 4}, [1, 2, 3], 'another object']
 --- check original and copy (deep copy) ---
[1, {1, 2, 3, 4, 10}, [1, 2, 3], 'another object']
[1, {1, 2, 3, 4}, [1, 2, 3], 'another object', 'one more object']
id(deep_copied_component.some_circular_ref.parent): 4340550880
id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent): 4340550880
^^ This shows that deepcopied objects contain same reference, they are not cloned repeatedly.
circular address check: 4340468048 / 4340550832
"""