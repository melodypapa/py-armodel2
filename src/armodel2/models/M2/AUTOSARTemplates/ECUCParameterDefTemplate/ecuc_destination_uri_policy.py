"""EcucDestinationUriPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 83)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcucDestinationUriPolicy(ARObject):
    """AUTOSAR EcucDestinationUriPolicy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ECUC-DESTINATION-URI-POLICY"


    containers: list[EcucContainerDef]
    destination_uri: Optional[Any]
    parameters: list[EcucParameterDef]
    reference_refs: list[Any]
    _DESERIALIZE_DISPATCH = {
        "CONTAINERS": ("_POLYMORPHIC_LIST", "containers", ["EcucChoiceContainerDef", "EcucParamConfContainerDef"]),
        "DESTINATION-URI": lambda obj, elem: setattr(obj, "destination_uri", SerializationHelper.deserialize_by_tag(elem, "any (EcucDestinationUri)")),
        "PARAMETERS": ("_POLYMORPHIC_LIST", "parameters", ["EcucAbstractStringParamDef", "EcucAddInfoParamDef", "EcucBooleanParamDef", "EcucEnumerationParamDef", "EcucFloatParamDef", "EcucIntegerParamDef"]),
        "REFERENCES": lambda obj, elem: obj.reference_refs.append(ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize EcucDestinationUriPolicy."""
        super().__init__()
        self.containers: list[EcucContainerDef] = []
        self.destination_uri: Optional[Any] = None
        self.parameters: list[EcucParameterDef] = []
        self.reference_refs: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize EcucDestinationUriPolicy to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucDestinationUriPolicy, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize containers (list to container "CONTAINERS")
        if self.containers:
            wrapper = ET.Element("CONTAINERS")
            for item in self.containers:
                serialized = SerializationHelper.serialize_item(item, "EcucContainerDef")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize destination_uri
        if self.destination_uri is not None:
            serialized = SerializationHelper.serialize_item(self.destination_uri, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESTINATION-URI")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize parameters (list to container "PARAMETERS")
        if self.parameters:
            wrapper = ET.Element("PARAMETERS")
            for item in self.parameters:
                serialized = SerializationHelper.serialize_item(item, "EcucParameterDef")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize reference_refs (list to container "REFERENCE-REFS")
        if self.reference_refs:
            wrapper = ET.Element("REFERENCE-REFS")
            for item in self.reference_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("REFERENCE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucDestinationUriPolicy":
        """Deserialize XML element to EcucDestinationUriPolicy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucDestinationUriPolicy object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucDestinationUriPolicy, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "CONTAINERS":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ECUC-CHOICE-CONTAINER-DEF":
                        obj.containers.append(SerializationHelper.deserialize_by_tag(child[0], "EcucChoiceContainerDef"))
                    elif concrete_tag == "ECUC-PARAM-CONF-CONTAINER-DEF":
                        obj.containers.append(SerializationHelper.deserialize_by_tag(child[0], "EcucParamConfContainerDef"))
            elif tag == "DESTINATION-URI":
                setattr(obj, "destination_uri", SerializationHelper.deserialize_by_tag(child, "any (EcucDestinationUri)"))
            elif tag == "PARAMETERS":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ECUC-ABSTRACT-STRING-PARAM-DEF":
                        obj.parameters.append(SerializationHelper.deserialize_by_tag(child[0], "EcucAbstractStringParamDef"))
                    elif concrete_tag == "ECUC-ADD-INFO-PARAM-DEF":
                        obj.parameters.append(SerializationHelper.deserialize_by_tag(child[0], "EcucAddInfoParamDef"))
                    elif concrete_tag == "ECUC-BOOLEAN-PARAM-DEF":
                        obj.parameters.append(SerializationHelper.deserialize_by_tag(child[0], "EcucBooleanParamDef"))
                    elif concrete_tag == "ECUC-ENUMERATION-PARAM-DEF":
                        obj.parameters.append(SerializationHelper.deserialize_by_tag(child[0], "EcucEnumerationParamDef"))
                    elif concrete_tag == "ECUC-FLOAT-PARAM-DEF":
                        obj.parameters.append(SerializationHelper.deserialize_by_tag(child[0], "EcucFloatParamDef"))
                    elif concrete_tag == "ECUC-INTEGER-PARAM-DEF":
                        obj.parameters.append(SerializationHelper.deserialize_by_tag(child[0], "EcucIntegerParamDef"))
            elif tag == "REFERENCES":
                obj.reference_refs.append(ARRef.deserialize(child))

        return obj



class EcucDestinationUriPolicyBuilder(BuilderBase):
    """Builder for EcucDestinationUriPolicy with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucDestinationUriPolicy = EcucDestinationUriPolicy()


    def with_containers(self, items: list[EcucContainerDef]) -> "EcucDestinationUriPolicyBuilder":
        """Set containers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.containers = list(items) if items else []
        return self

    def with_destination_uri(self, value: Optional[any (EcucDestinationUri)]) -> "EcucDestinationUriPolicyBuilder":
        """Set destination_uri attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.destination_uri = value
        return self

    def with_parameters(self, items: list[EcucParameterDef]) -> "EcucDestinationUriPolicyBuilder":
        """Set parameters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.parameters = list(items) if items else []
        return self

    def with_references(self, items: list[any (EcucAbstractReference)]) -> "EcucDestinationUriPolicyBuilder":
        """Set references list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.references = list(items) if items else []
        return self


    def add_container(self, item: EcucContainerDef) -> "EcucDestinationUriPolicyBuilder":
        """Add a single item to containers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.containers.append(item)
        return self

    def clear_containers(self) -> "EcucDestinationUriPolicyBuilder":
        """Clear all items from containers list.

        Returns:
            self for method chaining
        """
        self._obj.containers = []
        return self

    def add_parameter(self, item: EcucParameterDef) -> "EcucDestinationUriPolicyBuilder":
        """Add a single item to parameters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.parameters.append(item)
        return self

    def clear_parameters(self) -> "EcucDestinationUriPolicyBuilder":
        """Clear all items from parameters list.

        Returns:
            self for method chaining
        """
        self._obj.parameters = []
        return self

    def add_reference(self, item: any (EcucAbstractReference)) -> "EcucDestinationUriPolicyBuilder":
        """Add a single item to references list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.references.append(item)
        return self

    def clear_references(self) -> "EcucDestinationUriPolicyBuilder":
        """Clear all items from references list.

        Returns:
            self for method chaining
        """
        self._obj.references = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> EcucDestinationUriPolicy:
        """Build and return the EcucDestinationUriPolicy instance with validation."""
        self._validate_instance()
        pass
        return self._obj