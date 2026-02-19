"""ModeSwitchPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 323)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 633)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ModeDeclarationGroup.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeSwitchPoint(AbstractAccessPoint):
    """AUTOSAR ModeSwitchPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mode_group_swc_instance_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ModeSwitchPoint."""
        super().__init__()
        self.mode_group_swc_instance_ref: Optional[ARRef] = None
    def serialize(self) -> ET.Element:
        """Serialize ModeSwitchPoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModeSwitchPoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mode_group_swc_instance_ref
        if self.mode_group_swc_instance_ref is not None:
            serialized = ARObject._serialize_item(self.mode_group_swc_instance_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODE-GROUP-SWC-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeSwitchPoint":
        """Deserialize XML element to ModeSwitchPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeSwitchPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeSwitchPoint, cls).deserialize(element)

        # Parse mode_group_swc_instance_ref
        child = ARObject._find_child_element(element, "MODE-GROUP-SWC-INSTANCE-REF")
        if child is not None:
            mode_group_swc_instance_ref_value = ARRef.deserialize(child)
            obj.mode_group_swc_instance_ref = mode_group_swc_instance_ref_value

        return obj



class ModeSwitchPointBuilder:
    """Builder for ModeSwitchPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeSwitchPoint = ModeSwitchPoint()

    def build(self) -> ModeSwitchPoint:
        """Build and return ModeSwitchPoint object.

        Returns:
            ModeSwitchPoint instance
        """
        # TODO: Add validation
        return self._obj
