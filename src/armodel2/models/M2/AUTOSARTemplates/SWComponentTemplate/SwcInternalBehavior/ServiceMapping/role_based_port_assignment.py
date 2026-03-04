"""RoleBasedPortAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 329)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 166)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 604)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2050)

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
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
        PortPrototype,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class RoleBasedPortAssignment(ARObject):
    """AUTOSAR RoleBasedPortAssignment."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ROLE-BASED-PORT-ASSIGNMENT"


    port_prototype_ref: Optional[ARRef]
    role: Optional[Identifier]
    _DESERIALIZE_DISPATCH = {
        "PORT-PROTOTYPE-REF": ("_POLYMORPHIC", "port_prototype_ref", ["AbstractProvidedPortPrototype", "AbstractRequiredPortPrototype", "PPortPrototype", "PRPortPrototype", "RPortPrototype"]),
        "ROLE": lambda obj, elem: setattr(obj, "role", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
    }


    def __init__(self) -> None:
        """Initialize RoleBasedPortAssignment."""
        super().__init__()
        self.port_prototype_ref: Optional[ARRef] = None
        self.role: Optional[Identifier] = None

    def serialize(self) -> ET.Element:
        """Serialize RoleBasedPortAssignment to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RoleBasedPortAssignment, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize port_prototype_ref
        if self.port_prototype_ref is not None:
            serialized = SerializationHelper.serialize_item(self.port_prototype_ref, "PortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PORT-PROTOTYPE-REF")
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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RoleBasedPortAssignment":
        """Deserialize XML element to RoleBasedPortAssignment object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RoleBasedPortAssignment object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RoleBasedPortAssignment, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PORT-PROTOTYPE-REF":
                setattr(obj, "port_prototype_ref", ARRef.deserialize(child))
            elif tag == "ROLE":
                setattr(obj, "role", SerializationHelper.deserialize_by_tag(child, "Identifier"))

        return obj



class RoleBasedPortAssignmentBuilder(BuilderBase):
    """Builder for RoleBasedPortAssignment with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RoleBasedPortAssignment = RoleBasedPortAssignment()


    def with_port_prototype(self, value: Optional[PortPrototype]) -> "RoleBasedPortAssignmentBuilder":
        """Set port_prototype attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.port_prototype = value
        return self

    def with_role(self, value: Optional[Identifier]) -> "RoleBasedPortAssignmentBuilder":
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



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "portPrototype",
        "role",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> RoleBasedPortAssignment:
        """Build and return the RoleBasedPortAssignment instance with validation."""
        self._validate_instance()
        return self._obj