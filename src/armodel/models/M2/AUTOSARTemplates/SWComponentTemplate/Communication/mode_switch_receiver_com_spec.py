"""ModeSwitchReceiverComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 191)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeSwitchReceiverComSpec(RPortComSpec):
    """AUTOSAR ModeSwitchReceiverComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    enhanced_mode: Optional[Boolean]
    mode_group_ref: Optional[ARRef]
    supports: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize ModeSwitchReceiverComSpec."""
        super().__init__()
        self.enhanced_mode: Optional[Boolean] = None
        self.mode_group_ref: Optional[ARRef] = None
        self.supports: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize ModeSwitchReceiverComSpec to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModeSwitchReceiverComSpec, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize enhanced_mode
        if self.enhanced_mode is not None:
            serialized = SerializationHelper.serialize_item(self.enhanced_mode, "Boolean")
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

        # Serialize supports
        if self.supports is not None:
            serialized = SerializationHelper.serialize_item(self.supports, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUPPORTS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeSwitchReceiverComSpec":
        """Deserialize XML element to ModeSwitchReceiverComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeSwitchReceiverComSpec object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeSwitchReceiverComSpec, cls).deserialize(element)

        # Parse enhanced_mode
        child = SerializationHelper.find_child_element(element, "ENHANCED-MODE")
        if child is not None:
            enhanced_mode_value = child.text
            obj.enhanced_mode = enhanced_mode_value

        # Parse mode_group_ref
        child = SerializationHelper.find_child_element(element, "MODE-GROUP-REF")
        if child is not None:
            mode_group_ref_value = ARRef.deserialize(child)
            obj.mode_group_ref = mode_group_ref_value

        # Parse supports
        child = SerializationHelper.find_child_element(element, "SUPPORTS")
        if child is not None:
            supports_value = child.text
            obj.supports = supports_value

        return obj



class ModeSwitchReceiverComSpecBuilder:
    """Builder for ModeSwitchReceiverComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeSwitchReceiverComSpec = ModeSwitchReceiverComSpec()

    def build(self) -> ModeSwitchReceiverComSpec:
        """Build and return ModeSwitchReceiverComSpec object.

        Returns:
            ModeSwitchReceiverComSpec instance
        """
        # TODO: Add validation
        return self._obj
