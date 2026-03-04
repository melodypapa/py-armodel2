"""RoleBasedDataTypeAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 227)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 610)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_variable_ref import (
        AutosarVariableRef,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PerInstanceMemory.per_instance_memory import (
        PerInstanceMemory,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class RoleBasedDataTypeAssignment(ARObject):
    """AUTOSAR RoleBasedDataTypeAssignment."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ROLE-BASED-DATA-TYPE-ASSIGNMENT"


    role: Optional[Identifier]
    used_data_element: Optional[AutosarVariableRef]
    used_parameter_element: Optional[AutosarParameterRef ]
    used_pim_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "ROLE": lambda obj, elem: setattr(obj, "role", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
        "USED-DATA-ELEMENT": lambda obj, elem: setattr(obj, "used_data_element", SerializationHelper.deserialize_by_tag(elem, "AutosarVariableRef")),
        "USED-PARAMETER-ELEMENT": lambda obj, elem: setattr(obj, "used_parameter_element", SerializationHelper.deserialize_by_tag(elem, "AutosarParameterRef ")),
        "USED-PIM-REF": lambda obj, elem: setattr(obj, "used_pim_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize RoleBasedDataTypeAssignment."""
        super().__init__()
        self.role: Optional[Identifier] = None
        self.used_data_element: Optional[AutosarVariableRef] = None
        self.used_parameter_element: Optional[AutosarParameterRef ] = None
        self.used_pim_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize RoleBasedDataTypeAssignment to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RoleBasedDataTypeAssignment, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

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

        # Serialize used_data_element
        if self.used_data_element is not None:
            serialized = SerializationHelper.serialize_item(self.used_data_element, "AutosarVariableRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USED-DATA-ELEMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize used_parameter_element
        if self.used_parameter_element is not None:
            serialized = SerializationHelper.serialize_item(self.used_parameter_element, "AutosarParameterRef ")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USED-PARAMETER-ELEMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize used_pim_ref
        if self.used_pim_ref is not None:
            serialized = SerializationHelper.serialize_item(self.used_pim_ref, "PerInstanceMemory")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USED-PIM-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RoleBasedDataTypeAssignment":
        """Deserialize XML element to RoleBasedDataTypeAssignment object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RoleBasedDataTypeAssignment object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RoleBasedDataTypeAssignment, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ROLE":
                setattr(obj, "role", SerializationHelper.deserialize_by_tag(child, "Identifier"))
            elif tag == "USED-DATA-ELEMENT":
                setattr(obj, "used_data_element", SerializationHelper.deserialize_by_tag(child, "AutosarVariableRef"))
            elif tag == "USED-PARAMETER-ELEMENT":
                setattr(obj, "used_parameter_element", SerializationHelper.deserialize_by_tag(child, "AutosarParameterRef "))
            elif tag == "USED-PIM-REF":
                setattr(obj, "used_pim_ref", ARRef.deserialize(child))

        return obj



class RoleBasedDataTypeAssignmentBuilder(BuilderBase):
    """Builder for RoleBasedDataTypeAssignment with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RoleBasedDataTypeAssignment = RoleBasedDataTypeAssignment()


    def with_role(self, value: Optional[Identifier]) -> "RoleBasedDataTypeAssignmentBuilder":
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

    def with_used_data_element(self, value: Optional[AutosarVariableRef]) -> "RoleBasedDataTypeAssignmentBuilder":
        """Set used_data_element attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.used_data_element = value
        return self

    def with_used_parameter_element(self, value: Optional[AutosarParameterRef ]) -> "RoleBasedDataTypeAssignmentBuilder":
        """Set used_parameter_element attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.used_parameter_element = value
        return self

    def with_used_pim(self, value: Optional[PerInstanceMemory]) -> "RoleBasedDataTypeAssignmentBuilder":
        """Set used_pim attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.used_pim = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "role",
        "usedDataElement",
        "usedParameterElement",
        "usedPim",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> RoleBasedDataTypeAssignment:
        """Build and return the RoleBasedDataTypeAssignment instance with validation."""
        self._validate_instance()
        return self._obj