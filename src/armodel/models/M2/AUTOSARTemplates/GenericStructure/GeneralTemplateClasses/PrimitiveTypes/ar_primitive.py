"""ARPrimitive base class for all AUTOSAR primitive types."""

from __future__ import annotations
from typing import Optional, Any, get_type_hints, Union
import xml.etree.ElementTree as ET

from armodel.serialization.name_converter import NameConverter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class ARPrimitive:
    """Base class for all AUTOSAR primitive types.

    All primitive types (String, Integer, Float, etc.) inherit from this class.
    Provides common functionality for value wrapping and serialization.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self) -> None:
        """Initialize ARPrimitive."""
        super().__init__()
        self.value: Optional[Any] = None

    def _get_xml_tag(self) -> str:
        """Get XML tag name for this class.

        Auto-generates from class name using NameConverter.

        Returns:
            XML tag name
        """
        return NameConverter.to_xml_tag(self.__class__.__name__)

    def serialize(self, namespace: str = "") -> ET.Element:
        """Serialize the primitive to an XML element.

        Serializes the value as element text content and any additional
        attributes as XML attributes.

        Args:
            namespace: XML namespace URI (optional)

        Returns:
            xml.etree.ElementTree.Element representing this primitive
        """
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        if namespace:
            elem.set("xmlns", namespace)

        # Serialize value as text content
        if self.value is not None:
            elem.text = str(self.value)

        # Serialize additional attributes as XML attributes
        # Get all instance attributes excluding 'value' and private attributes
        for name, value in vars(self).items():
            if name.startswith('_') or name == 'value':
                continue

            # Convert Python name to XML tag
            xml_tag = NameConverter.to_xml_tag(name)

            # Skip None values
            if value is None:
                continue

            # Serialize as XML attribute
            if hasattr(value, 'value'):
                # Handle primitive types with value attribute
                # Check if it's an AREnum and convert to uppercase
                if isinstance(value, AREnum):
                    elem.set(xml_tag, str(value.value).upper())
                else:
                    elem.set(xml_tag, str(value.value))
            else:
                elem.set(xml_tag, str(value))

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ARPrimitive":
        """Deserialize an XML element to an ARPrimitive instance.

        Automatically converts the text content to the appropriate Python type
        based on the python_type class attribute. Also deserializes any
        additional XML attributes to object attributes.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ARPrimitive instance
        """
        # Get type hints to know what attributes to expect
        type_hints = {}
        try:
            type_hints = get_type_hints(cls)
        except Exception:
            # Fallback: Use __annotations__ directly if get_type_hints fails
            # Note: Annotations will be strings due to 'from __future__ import annotations'
            if hasattr(cls, '__annotations__'):
                for attr_name, attr_type_str in cls.__annotations__.items():
                    if attr_name != 'value':  # Skip value, it's handled separately
                        type_hints[attr_name] = attr_type_str

        # Get __init__ signature to determine which parameters to pass
        import inspect
        init_signature = inspect.signature(cls.__init__)
        init_params = list(init_signature.parameters.keys())
        init_params.remove('self')  # Remove 'self'

        # Collect attribute values from XML
        attr_values = {'value': None}
        for param_name in init_params:
            if param_name == 'value':
                continue

            # Convert Python name to XML tag
            xml_tag = NameConverter.to_xml_tag(param_name)

            # Get attribute value from XML
            attr_value = element.get(xml_tag)

            # Convert to appropriate type based on type hints
            if param_name in type_hints and attr_value is not None:
                attr_type = type_hints[param_name]
                
                # Unwrap Optional type if present
                from typing import get_origin, get_args
                origin = get_origin(attr_type)
                if origin is Union:
                    type_args = get_args(attr_type)
                    # Get the first non-None type
                    for arg in type_args:
                        if arg is not type(None):
                            attr_type = arg
                            break
                
                # Check if it's an AREnum type
                if isinstance(attr_type, type) and issubclass(attr_type, AREnum):
                    # Deserialize as enum by creating a fake XML element
                    fake_elem = ET.Element('TEMP')
                    fake_elem.text = attr_value
                    attr_values[param_name] = attr_type.deserialize(fake_elem)
                else:
                    # Simple type conversion for other types
                    attr_values[param_name] = str(attr_value)
            elif attr_value is not None:
                attr_values[param_name] = attr_value

        # Deserialize text content to value
        if element.text:
            # Convert to the appropriate Python type based on python_type
            if cls.python_type is str:
                attr_values['value'] = element.text
            elif cls.python_type is int:
                try:
                    attr_values['value'] = int(element.text)
                except ValueError:
                    attr_values['value'] = element.text  # Keep as string if conversion fails
            elif cls.python_type is float:
                try:
                    attr_values['value'] = float(element.text)
                except ValueError:
                    attr_values['value'] = element.text
            elif cls.python_type is bool:
                attr_values['value'] = element.text.lower() in ('true', '1', 'yes')
            else:
                attr_values['value'] = element.text

        # Create instance with all parameters
        obj = cls(**attr_values)

        return obj

    def __str__(self) -> str:
        """Return string representation of the primitive value."""
        return str(self.value) if self.value is not None else ""

    def __repr__(self) -> str:
        """Return detailed string representation."""
        return f"{self.__class__.__name__}({self.value!r})"

    def __eq__(self, other: object) -> bool:
        """Check equality based on value.

        Provides transparent comparison with primitive Python types (str, int, float, bool).

        Args:
            other: Object to compare with

        Returns:
            True if values are equal (both same class or primitive type), False otherwise
        """
        # Compare with same class (existing behavior)
        if isinstance(other, self.__class__):
            return self.value == other.value
        # Compare with primitive Python type (transparent behavior)
        if isinstance(other, self.python_type):
            return self.value == other
        return NotImplemented

    def __hash__(self) -> int:
        """Return hash based on value.

        Returns:
            Hash of the value, or hash of None if value is None
        """
        return hash(self.value) if self.value is not None else hash(None)
