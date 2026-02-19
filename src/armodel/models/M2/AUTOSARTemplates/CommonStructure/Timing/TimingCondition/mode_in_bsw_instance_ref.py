"""ModeInBswInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 38)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation.bsw_implementation import (
    BswImplementation,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeInBswInstanceRef(ARObject):
    """AUTOSAR ModeInBswInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_bsw: Optional[BswImplementation]
    context_mode_ref: Optional[ARRef]
    target_mode: Optional[ModeDeclaration]
    def __init__(self) -> None:
        """Initialize ModeInBswInstanceRef."""
        super().__init__()
        self.context_bsw: Optional[BswImplementation] = None
        self.context_mode_ref: Optional[ARRef] = None
        self.target_mode: Optional[ModeDeclaration] = None
    def serialize(self) -> ET.Element:
        """Serialize ModeInBswInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize context_bsw
        if self.context_bsw is not None:
            serialized = ARObject._serialize_item(self.context_bsw, "BswImplementation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-BSW")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_mode_ref
        if self.context_mode_ref is not None:
            serialized = ARObject._serialize_item(self.context_mode_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_mode
        if self.target_mode is not None:
            serialized = ARObject._serialize_item(self.target_mode, "ModeDeclaration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeInBswInstanceRef":
        """Deserialize XML element to ModeInBswInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeInBswInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse context_bsw
        child = ARObject._find_child_element(element, "CONTEXT-BSW")
        if child is not None:
            context_bsw_value = ARObject._deserialize_by_tag(child, "BswImplementation")
            obj.context_bsw = context_bsw_value

        # Parse context_mode_ref
        child = ARObject._find_child_element(element, "CONTEXT-MODE-REF")
        if child is not None:
            context_mode_ref_value = ARRef.deserialize(child)
            obj.context_mode_ref = context_mode_ref_value

        # Parse target_mode
        child = ARObject._find_child_element(element, "TARGET-MODE")
        if child is not None:
            target_mode_value = ARObject._deserialize_by_tag(child, "ModeDeclaration")
            obj.target_mode = target_mode_value

        return obj



class ModeInBswInstanceRefBuilder:
    """Builder for ModeInBswInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeInBswInstanceRef = ModeInBswInstanceRef()

    def build(self) -> ModeInBswInstanceRef:
        """Build and return ModeInBswInstanceRef object.

        Returns:
            ModeInBswInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
