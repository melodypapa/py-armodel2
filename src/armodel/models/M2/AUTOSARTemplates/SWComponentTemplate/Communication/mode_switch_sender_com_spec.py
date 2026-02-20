"""ModeSwitchSenderComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 190)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeSwitchSenderComSpec(PPortComSpec):
    """AUTOSAR ModeSwitchSenderComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    enhanced_mode: Optional[Boolean]
    mode_group_ref: Optional[ARRef]
    mode_switched_ack: Optional[Any]
    queue_length: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize ModeSwitchSenderComSpec."""
        super().__init__()
        self.enhanced_mode: Optional[Boolean] = None
        self.mode_group_ref: Optional[ARRef] = None
        self.mode_switched_ack: Optional[Any] = None
        self.queue_length: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize ModeSwitchSenderComSpec to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModeSwitchSenderComSpec, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize enhanced_mode
        if self.enhanced_mode is not None:
            serialized = ARObject._serialize_item(self.enhanced_mode, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENHANCED-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mode_group_ref
        if self.mode_group_ref is not None:
            serialized = ARObject._serialize_item(self.mode_group_ref, "ModeDeclarationGroup")
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

        # Serialize mode_switched_ack
        if self.mode_switched_ack is not None:
            serialized = ARObject._serialize_item(self.mode_switched_ack, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODE-SWITCHED-ACK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize queue_length
        if self.queue_length is not None:
            serialized = ARObject._serialize_item(self.queue_length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("QUEUE-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeSwitchSenderComSpec":
        """Deserialize XML element to ModeSwitchSenderComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeSwitchSenderComSpec object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeSwitchSenderComSpec, cls).deserialize(element)

        # Parse enhanced_mode
        child = ARObject._find_child_element(element, "ENHANCED-MODE")
        if child is not None:
            enhanced_mode_value = child.text
            obj.enhanced_mode = enhanced_mode_value

        # Parse mode_group_ref
        child = ARObject._find_child_element(element, "MODE-GROUP-REF")
        if child is not None:
            mode_group_ref_value = ARRef.deserialize(child)
            obj.mode_group_ref = mode_group_ref_value

        # Parse mode_switched_ack
        child = ARObject._find_child_element(element, "MODE-SWITCHED-ACK")
        if child is not None:
            mode_switched_ack_value = child.text
            obj.mode_switched_ack = mode_switched_ack_value

        # Parse queue_length
        child = ARObject._find_child_element(element, "QUEUE-LENGTH")
        if child is not None:
            queue_length_value = child.text
            obj.queue_length = queue_length_value

        return obj



class ModeSwitchSenderComSpecBuilder:
    """Builder for ModeSwitchSenderComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeSwitchSenderComSpec = ModeSwitchSenderComSpec()

    def build(self) -> ModeSwitchSenderComSpec:
        """Build and return ModeSwitchSenderComSpec object.

        Returns:
            ModeSwitchSenderComSpec instance
        """
        # TODO: Add validation
        return self._obj
