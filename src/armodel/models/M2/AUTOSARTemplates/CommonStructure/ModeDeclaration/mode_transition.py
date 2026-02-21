"""ModeTransition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 43)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 630)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ModeDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class ModeTransition(Identifiable):
    """AUTOSAR ModeTransition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    entered_mode_ref: Optional[ARRef]
    exited_mode_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ModeTransition."""
        super().__init__()
        self.entered_mode_ref: Optional[ARRef] = None
        self.exited_mode_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ModeTransition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModeTransition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize entered_mode_ref
        if self.entered_mode_ref is not None:
            serialized = ARObject._serialize_item(self.entered_mode_ref, "ModeDeclaration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENTERED-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize exited_mode_ref
        if self.exited_mode_ref is not None:
            serialized = ARObject._serialize_item(self.exited_mode_ref, "ModeDeclaration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXITED-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeTransition":
        """Deserialize XML element to ModeTransition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeTransition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeTransition, cls).deserialize(element)

        # Parse entered_mode_ref
        child = ARObject._find_child_element(element, "ENTERED-MODE-REF")
        if child is not None:
            entered_mode_ref_value = ARRef.deserialize(child)
            obj.entered_mode_ref = entered_mode_ref_value

        # Parse exited_mode_ref
        child = ARObject._find_child_element(element, "EXITED-MODE-REF")
        if child is not None:
            exited_mode_ref_value = ARRef.deserialize(child)
            obj.exited_mode_ref = exited_mode_ref_value

        return obj



class ModeTransitionBuilder:
    """Builder for ModeTransition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeTransition = ModeTransition()

    def build(self) -> ModeTransition:
        """Build and return ModeTransition object.

        Returns:
            ModeTransition instance
        """
        # TODO: Add validation
        return self._obj
