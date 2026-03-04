"""EcucParamConfContainerDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 39)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import EcucContainerDefBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcucParamConfContainerDef(EcucContainerDef):
    """AUTOSAR EcucParamConfContainerDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ECUC-PARAM-CONF-CONTAINER-DEF"


    parameters: list[EcucParameterDef]
    reference_refs: list[Any]
    sub_containers: list[EcucContainerDef]
    _DESERIALIZE_DISPATCH = {
        "PARAMETERS": ("_POLYMORPHIC_LIST", "parameters", ["EcucAbstractStringParamDef", "EcucAddInfoParamDef", "EcucBooleanParamDef", "EcucEnumerationParamDef", "EcucFloatParamDef", "EcucFunctionNameDef", "EcucIntegerParamDef", "EcucLinkerSymbolDef", "EcucMultilineStringParamDef", "EcucStringParamDef"]),
        "REFERENCE-REFS": lambda obj, elem: [obj.reference_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "SUB-CONTAINERS": ("_POLYMORPHIC_LIST", "sub_containers", ["EcucChoiceContainerDef", "EcucParamConfContainerDef"]),
    }


    def __init__(self) -> None:
        """Initialize EcucParamConfContainerDef."""
        super().__init__()
        self.parameters: list[EcucParameterDef] = []
        self.reference_refs: list[Any] = []
        self.sub_containers: list[EcucContainerDef] = []

    def serialize(self) -> ET.Element:
        """Serialize EcucParamConfContainerDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucParamConfContainerDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

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

        # Serialize sub_containers (list to container "SUB-CONTAINERS")
        if self.sub_containers:
            wrapper = ET.Element("SUB-CONTAINERS")
            for item in self.sub_containers:
                serialized = SerializationHelper.serialize_item(item, "EcucContainerDef")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucParamConfContainerDef":
        """Deserialize XML element to EcucParamConfContainerDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucParamConfContainerDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucParamConfContainerDef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PARAMETERS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "ECUC-ABSTRACT-STRING-PARAM-DEF":
                        obj.parameters.append(SerializationHelper.deserialize_by_tag(item_elem, "EcucAbstractStringParamDef"))
                    elif concrete_tag == "ECUC-ADD-INFO-PARAM-DEF":
                        obj.parameters.append(SerializationHelper.deserialize_by_tag(item_elem, "EcucAddInfoParamDef"))
                    elif concrete_tag == "ECUC-BOOLEAN-PARAM-DEF":
                        obj.parameters.append(SerializationHelper.deserialize_by_tag(item_elem, "EcucBooleanParamDef"))
                    elif concrete_tag == "ECUC-ENUMERATION-PARAM-DEF":
                        obj.parameters.append(SerializationHelper.deserialize_by_tag(item_elem, "EcucEnumerationParamDef"))
                    elif concrete_tag == "ECUC-FLOAT-PARAM-DEF":
                        obj.parameters.append(SerializationHelper.deserialize_by_tag(item_elem, "EcucFloatParamDef"))
                    elif concrete_tag == "ECUC-FUNCTION-NAME-DEF":
                        obj.parameters.append(SerializationHelper.deserialize_by_tag(item_elem, "EcucFunctionNameDef"))
                    elif concrete_tag == "ECUC-INTEGER-PARAM-DEF":
                        obj.parameters.append(SerializationHelper.deserialize_by_tag(item_elem, "EcucIntegerParamDef"))
                    elif concrete_tag == "ECUC-LINKER-SYMBOL-DEF":
                        obj.parameters.append(SerializationHelper.deserialize_by_tag(item_elem, "EcucLinkerSymbolDef"))
                    elif concrete_tag == "ECUC-MULTILINE-STRING-PARAM-DEF":
                        obj.parameters.append(SerializationHelper.deserialize_by_tag(item_elem, "EcucMultilineStringParamDef"))
                    elif concrete_tag == "ECUC-STRING-PARAM-DEF":
                        obj.parameters.append(SerializationHelper.deserialize_by_tag(item_elem, "EcucStringParamDef"))
            elif tag == "REFERENCE-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.reference_refs.append(ARRef.deserialize(item_elem))
            elif tag == "SUB-CONTAINERS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "ECUC-CHOICE-CONTAINER-DEF":
                        obj.sub_containers.append(SerializationHelper.deserialize_by_tag(item_elem, "EcucChoiceContainerDef"))
                    elif concrete_tag == "ECUC-PARAM-CONF-CONTAINER-DEF":
                        obj.sub_containers.append(SerializationHelper.deserialize_by_tag(item_elem, "EcucParamConfContainerDef"))

        return obj



class EcucParamConfContainerDefBuilder(EcucContainerDefBuilder):
    """Builder for EcucParamConfContainerDef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucParamConfContainerDef = EcucParamConfContainerDef()


    def with_parameters(self, items: list[EcucParameterDef]) -> "EcucParamConfContainerDefBuilder":
        """Set parameters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.parameters = list(items) if items else []
        return self

    def with_references(self, items: list[any (EcucAbstractReference)]) -> "EcucParamConfContainerDefBuilder":
        """Set references list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.references = list(items) if items else []
        return self

    def with_sub_containers(self, items: list[EcucContainerDef]) -> "EcucParamConfContainerDefBuilder":
        """Set sub_containers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sub_containers = list(items) if items else []
        return self


    def add_parameter(self, item: EcucParameterDef) -> "EcucParamConfContainerDefBuilder":
        """Add a single item to parameters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.parameters.append(item)
        return self

    def clear_parameters(self) -> "EcucParamConfContainerDefBuilder":
        """Clear all items from parameters list.

        Returns:
            self for method chaining
        """
        self._obj.parameters = []
        return self

    def add_reference(self, item: any (EcucAbstractReference)) -> "EcucParamConfContainerDefBuilder":
        """Add a single item to references list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.references.append(item)
        return self

    def clear_references(self) -> "EcucParamConfContainerDefBuilder":
        """Clear all items from references list.

        Returns:
            self for method chaining
        """
        self._obj.references = []
        return self

    def add_sub_container(self, item: EcucContainerDef) -> "EcucParamConfContainerDefBuilder":
        """Add a single item to sub_containers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sub_containers.append(item)
        return self

    def clear_sub_containers(self) -> "EcucParamConfContainerDefBuilder":
        """Clear all items from sub_containers list.

        Returns:
            self for method chaining
        """
        self._obj.sub_containers = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "parameter",
        "reference",
        "subContainer",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EcucParamConfContainerDef:
        """Build and return the EcucParamConfContainerDef instance with validation."""
        self._validate_instance()
        return self._obj