"""ModeInBswModuleDescriptionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 323)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswOverview_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview.bsw_module_description import (
    BswModuleDescription,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeInBswModuleDescriptionInstanceRef(ARObject):
    """AUTOSAR ModeInBswModuleDescriptionInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base: Optional[BswModuleDescription]
    context_mode_group_ref: Optional[ARRef]
    target_mode: Optional[ModeDeclaration]
    def __init__(self) -> None:
        """Initialize ModeInBswModuleDescriptionInstanceRef."""
        super().__init__()
        self.base: Optional[BswModuleDescription] = None
        self.context_mode_group_ref: Optional[ARRef] = None
        self.target_mode: Optional[ModeDeclaration] = None
    def serialize(self) -> ET.Element:
        """Serialize ModeInBswModuleDescriptionInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize base
        if self.base is not None:
            serialized = ARObject._serialize_item(self.base, "BswModuleDescription")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_mode_group_ref
        if self.context_mode_group_ref is not None:
            serialized = ARObject._serialize_item(self.context_mode_group_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-MODE-GROUP")
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
    def deserialize(cls, element: ET.Element) -> "ModeInBswModuleDescriptionInstanceRef":
        """Deserialize XML element to ModeInBswModuleDescriptionInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeInBswModuleDescriptionInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base
        child = ARObject._find_child_element(element, "BASE")
        if child is not None:
            base_value = ARObject._deserialize_by_tag(child, "BswModuleDescription")
            obj.base = base_value

        # Parse context_mode_group_ref
        child = ARObject._find_child_element(element, "CONTEXT-MODE-GROUP")
        if child is not None:
            context_mode_group_ref_value = ARObject._deserialize_by_tag(child, "ModeDeclarationGroup")
            obj.context_mode_group_ref = context_mode_group_ref_value

        # Parse target_mode
        child = ARObject._find_child_element(element, "TARGET-MODE")
        if child is not None:
            target_mode_value = ARObject._deserialize_by_tag(child, "ModeDeclaration")
            obj.target_mode = target_mode_value

        return obj



class ModeInBswModuleDescriptionInstanceRefBuilder:
    """Builder for ModeInBswModuleDescriptionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeInBswModuleDescriptionInstanceRef = ModeInBswModuleDescriptionInstanceRef()

    def build(self) -> ModeInBswModuleDescriptionInstanceRef:
        """Build and return ModeInBswModuleDescriptionInstanceRef object.

        Returns:
            ModeInBswModuleDescriptionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
