"""ModeInBswModuleDescriptionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 323)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswOverview_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
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

    base_ref: Optional[ARRef]
    context_mode_group_ref: Optional[ARRef]
    target_mode_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ModeInBswModuleDescriptionInstanceRef."""
        super().__init__()
        self.base_ref: Optional[ARRef] = None
        self.context_mode_group_ref: Optional[ARRef] = None
        self.target_mode_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ModeInBswModuleDescriptionInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize base_ref
        if self.base_ref is not None:
            serialized = SerializationHelper.serialize_item(self.base_ref, "BswModuleDescription")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_mode_group_ref
        if self.context_mode_group_ref is not None:
            serialized = SerializationHelper.serialize_item(self.context_mode_group_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-MODE-GROUP-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_mode_ref
        if self.target_mode_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_mode_ref, "ModeDeclaration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-MODE-REF")
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

        # Parse base_ref
        child = SerializationHelper.find_child_element(element, "BASE-REF")
        if child is not None:
            base_ref_value = ARRef.deserialize(child)
            obj.base_ref = base_ref_value

        # Parse context_mode_group_ref
        child = SerializationHelper.find_child_element(element, "CONTEXT-MODE-GROUP-REF")
        if child is not None:
            context_mode_group_ref_value = ARRef.deserialize(child)
            obj.context_mode_group_ref = context_mode_group_ref_value

        # Parse target_mode_ref
        child = SerializationHelper.find_child_element(element, "TARGET-MODE-REF")
        if child is not None:
            target_mode_ref_value = ARRef.deserialize(child)
            obj.target_mode_ref = target_mode_ref_value

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
