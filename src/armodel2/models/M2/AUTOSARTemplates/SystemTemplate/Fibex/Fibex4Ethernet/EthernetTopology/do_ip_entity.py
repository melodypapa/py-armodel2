"""DoIpEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 471)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    DoIpEntityRoleEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DoIpEntity(ARObject):
    """AUTOSAR DoIpEntity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DO-IP-ENTITY"


    do_ip_entity_role_enum: Optional[DoIpEntityRoleEnum]
    _DESERIALIZE_DISPATCH = {
        "DO-IP-ENTITY-ROLE-ENUM": lambda obj, elem: setattr(obj, "do_ip_entity_role_enum", DoIpEntityRoleEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DoIpEntity."""
        super().__init__()
        self.do_ip_entity_role_enum: Optional[DoIpEntityRoleEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize DoIpEntity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DoIpEntity, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize do_ip_entity_role_enum
        if self.do_ip_entity_role_enum is not None:
            serialized = SerializationHelper.serialize_item(self.do_ip_entity_role_enum, "DoIpEntityRoleEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DO-IP-ENTITY-ROLE-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpEntity":
        """Deserialize XML element to DoIpEntity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DoIpEntity object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DoIpEntity, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DO-IP-ENTITY-ROLE-ENUM":
                setattr(obj, "do_ip_entity_role_enum", DoIpEntityRoleEnum.deserialize(child))

        return obj



class DoIpEntityBuilder(BuilderBase):
    """Builder for DoIpEntity with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DoIpEntity = DoIpEntity()


    def with_do_ip_entity_role_enum(self, value: Optional[DoIpEntityRoleEnum]) -> "DoIpEntityBuilder":
        """Set do_ip_entity_role_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'do_ip_entity_role_enum' is required and cannot be None")
        self._obj.do_ip_entity_role_enum = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "doIpEntityRoleEnum",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DoIpEntity:
        """Build and return the DoIpEntity instance with validation."""
        self._validate_instance()
        return self._obj