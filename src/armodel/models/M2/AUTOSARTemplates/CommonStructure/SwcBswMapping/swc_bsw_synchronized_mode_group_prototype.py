"""SwcBswSynchronizedModeGroupPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 111)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SwcBswMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class SwcBswSynchronizedModeGroupPrototype(ARObject):
    """AUTOSAR SwcBswSynchronizedModeGroupPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_mode_group_prototype_ref: Optional[ARRef]
    swc_mode_group_swc_instance_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SwcBswSynchronizedModeGroupPrototype."""
        super().__init__()
        self.bsw_mode_group_prototype_ref: Optional[ARRef] = None
        self.swc_mode_group_swc_instance_ref: Optional[ARRef] = None
    def serialize(self) -> ET.Element:
        """Serialize SwcBswSynchronizedModeGroupPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize bsw_mode_group_prototype_ref
        if self.bsw_mode_group_prototype_ref is not None:
            serialized = ARObject._serialize_item(self.bsw_mode_group_prototype_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-MODE-GROUP-PROTOTYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize swc_mode_group_swc_instance_ref
        if self.swc_mode_group_swc_instance_ref is not None:
            serialized = ARObject._serialize_item(self.swc_mode_group_swc_instance_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SWC-MODE-GROUP-SWC-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcBswSynchronizedModeGroupPrototype":
        """Deserialize XML element to SwcBswSynchronizedModeGroupPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcBswSynchronizedModeGroupPrototype object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bsw_mode_group_prototype_ref
        child = ARObject._find_child_element(element, "BSW-MODE-GROUP-PROTOTYPE")
        if child is not None:
            bsw_mode_group_prototype_ref_value = ARObject._deserialize_by_tag(child, "ModeDeclarationGroup")
            obj.bsw_mode_group_prototype_ref = bsw_mode_group_prototype_ref_value

        # Parse swc_mode_group_swc_instance_ref
        child = ARObject._find_child_element(element, "SWC-MODE-GROUP-SWC-INSTANCE-REF")
        if child is not None:
            swc_mode_group_swc_instance_ref_value = ARObject._deserialize_by_tag(child, "ModeDeclarationGroup")
            obj.swc_mode_group_swc_instance_ref = swc_mode_group_swc_instance_ref_value

        return obj



class SwcBswSynchronizedModeGroupPrototypeBuilder:
    """Builder for SwcBswSynchronizedModeGroupPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcBswSynchronizedModeGroupPrototype = SwcBswSynchronizedModeGroupPrototype()

    def build(self) -> SwcBswSynchronizedModeGroupPrototype:
        """Build and return SwcBswSynchronizedModeGroupPrototype object.

        Returns:
            SwcBswSynchronizedModeGroupPrototype instance
        """
        # TODO: Add validation
        return self._obj
