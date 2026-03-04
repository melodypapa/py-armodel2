"""BuildActionIoElement AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 368)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_BuildActionManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    NameToken,
)
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import (
    EcucDefinitionElement,
)
from armodel2.models.M2.MSR.AsamHdo.SpecialData.sdg import (
    Sdg,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BuildActionIoElement(ARObject):
    """AUTOSAR BuildActionIoElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BUILD-ACTION-IO-ELEMENT"


    category: NameToken
    ecuc_definition_ref: Optional[ARRef]
    role: Optional[Identifier]
    sdgs: list[Sdg]
    _DESERIALIZE_DISPATCH = {
        "CATEGORY": lambda obj, elem: setattr(obj, "category", SerializationHelper.deserialize_by_tag(elem, "NameToken")),
        "ECUC-DEFINITION-REF": ("_POLYMORPHIC", "ecuc_definition_ref", ["EcucAddInfoParamDef", "EcucBooleanParamDef", "EcucChoiceContainerDef", "EcucChoiceReferenceDef", "EcucCommonAttributes", "EcucContainerDef", "EcucEnumerationParamDef", "EcucFloatParamDef", "EcucForeignReferenceDef", "EcucFunctionNameDef", "EcucInstanceReferenceDef", "EcucIntegerParamDef", "EcucLinkerSymbolDef", "EcucModuleDef", "EcucMultilineStringParamDef", "EcucParamConfContainerDef", "EcucReferenceDef", "EcucStringParamDef", "EcucUriReferenceDef"]),
        "ROLE": lambda obj, elem: setattr(obj, "role", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
        "SDGS": lambda obj, elem: obj.sdgs.append(SerializationHelper.deserialize_by_tag(elem, "Sdg")),
    }


    def __init__(self) -> None:
        """Initialize BuildActionIoElement."""
        super().__init__()
        self.category: NameToken = None
        self.ecuc_definition_ref: Optional[ARRef] = None
        self.role: Optional[Identifier] = None
        self.sdgs: list[Sdg] = []

    def serialize(self) -> ET.Element:
        """Serialize BuildActionIoElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BuildActionIoElement, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize category
        if self.category is not None:
            serialized = SerializationHelper.serialize_item(self.category, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CATEGORY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecuc_definition_ref
        if self.ecuc_definition_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ecuc_definition_ref, "EcucDefinitionElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECUC-DEFINITION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize role
        if self.role is not None:
            serialized = SerializationHelper.serialize_item(self.role, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdgs (list to container "SDGS")
        if self.sdgs:
            wrapper = ET.Element("SDGS")
            for item in self.sdgs:
                serialized = SerializationHelper.serialize_item(item, "Sdg")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BuildActionIoElement":
        """Deserialize XML element to BuildActionIoElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BuildActionIoElement object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BuildActionIoElement, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CATEGORY":
                setattr(obj, "category", SerializationHelper.deserialize_by_tag(child, "NameToken"))
            elif tag == "ECUC-DEFINITION-REF":
                setattr(obj, "ecuc_definition_ref", ARRef.deserialize(child))
            elif tag == "ROLE":
                setattr(obj, "role", SerializationHelper.deserialize_by_tag(child, "Identifier"))
            elif tag == "SDGS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.sdgs.append(SerializationHelper.deserialize_by_tag(item_elem, "Sdg"))

        return obj



class BuildActionIoElementBuilder(BuilderBase):
    """Builder for BuildActionIoElement with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BuildActionIoElement = BuildActionIoElement()


    def with_category(self, value: NameToken) -> "BuildActionIoElementBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_ecuc_definition(self, value: Optional[EcucDefinitionElement]) -> "BuildActionIoElementBuilder":
        """Set ecuc_definition attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ecuc_definition = value
        return self

    def with_role(self, value: Optional[Identifier]) -> "BuildActionIoElementBuilder":
        """Set role attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.role = value
        return self

    def with_sdgs(self, items: list[Sdg]) -> "BuildActionIoElementBuilder":
        """Set sdgs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sdgs = list(items) if items else []
        return self


    def add_sdg(self, item: Sdg) -> "BuildActionIoElementBuilder":
        """Add a single item to sdgs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sdgs.append(item)
        return self

    def clear_sdgs(self) -> "BuildActionIoElementBuilder":
        """Clear all items from sdgs list.

        Returns:
            self for method chaining
        """
        self._obj.sdgs = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "category",
    }
    _OPTIONAL_ATTRIBUTES = {
        "ecucDefinition",
        "role",
        "sdg",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "category", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError(f"Required attribute 'category' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn(f"Required attribute 'category' is None", UserWarning)


    def build(self) -> BuildActionIoElement:
        """Build and return the BuildActionIoElement instance with validation."""
        self._validate_instance()
        return self._obj