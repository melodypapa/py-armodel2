"""ModeRequestTypeMap AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 44)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 115)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ModeDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
        AbstractImplementationDataType,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class ModeRequestTypeMap(ARObject):
    """AUTOSAR ModeRequestTypeMap."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MODE-REQUEST-TYPE-MAP"


    implementation_data_type_ref: Optional[ARRef]
    mode_group_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "IMPLEMENTATION-DATA-TYPE-REF": ("_POLYMORPHIC", "implementation_data_type_ref", ["ImplementationDataType"]),
        "MODE-GROUP-REF": lambda obj, elem: setattr(obj, "mode_group_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ModeRequestTypeMap."""
        super().__init__()
        self.implementation_data_type_ref: Optional[ARRef] = None
        self.mode_group_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ModeRequestTypeMap to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModeRequestTypeMap, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize implementation_data_type_ref
        if self.implementation_data_type_ref is not None:
            serialized = SerializationHelper.serialize_item(self.implementation_data_type_ref, "AbstractImplementationDataType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IMPLEMENTATION-DATA-TYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mode_group_ref
        if self.mode_group_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mode_group_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODE-GROUP-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeRequestTypeMap":
        """Deserialize XML element to ModeRequestTypeMap object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeRequestTypeMap object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeRequestTypeMap, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "IMPLEMENTATION-DATA-TYPE-REF":
                setattr(obj, "implementation_data_type_ref", ARRef.deserialize(child))
            elif tag == "MODE-GROUP-REF":
                setattr(obj, "mode_group_ref", ARRef.deserialize(child))

        return obj



class ModeRequestTypeMapBuilder(BuilderBase):
    """Builder for ModeRequestTypeMap with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ModeRequestTypeMap = ModeRequestTypeMap()


    def with_implementation_data_type(self, value: Optional[AbstractImplementationDataType]) -> "ModeRequestTypeMapBuilder":
        """Set implementation_data_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.implementation_data_type = value
        return self

    def with_mode_group(self, value: Optional[ModeDeclarationGroup]) -> "ModeRequestTypeMapBuilder":
        """Set mode_group attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mode_group = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "implementationDataType",
        "modeGroup",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ModeRequestTypeMap:
        """Build and return the ModeRequestTypeMap instance with validation."""
        self._validate_instance()
        return self._obj