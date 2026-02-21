"""ModeAccessPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 323)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 634)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ModeDeclarationGroup.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.mode_access_point_ident import (
    ModeAccessPointIdent,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeAccessPoint(ARObject):
    """AUTOSAR ModeAccessPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ident: Optional[ModeAccessPointIdent]
    mode_group_instance_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ModeAccessPoint."""
        super().__init__()
        self.ident: Optional[ModeAccessPointIdent] = None
        self.mode_group_instance_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ModeAccessPoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModeAccessPoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ident
        if self.ident is not None:
            serialized = SerializationHelper.serialize_item(self.ident, "ModeAccessPointIdent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mode_group_instance_ref
        if self.mode_group_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mode_group_instance_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODE-GROUP-INSTANCE-REF-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeAccessPoint":
        """Deserialize XML element to ModeAccessPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeAccessPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeAccessPoint, cls).deserialize(element)

        # Parse ident
        child = SerializationHelper.find_child_element(element, "IDENT")
        if child is not None:
            ident_value = SerializationHelper.deserialize_by_tag(child, "ModeAccessPointIdent")
            obj.ident = ident_value

        # Parse mode_group_instance_ref
        child = SerializationHelper.find_child_element(element, "MODE-GROUP-INSTANCE-REF-REF")
        if child is not None:
            mode_group_instance_ref_value = ARRef.deserialize(child)
            obj.mode_group_instance_ref = mode_group_instance_ref_value

        return obj



class ModeAccessPointBuilder:
    """Builder for ModeAccessPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeAccessPoint = ModeAccessPoint()

    def build(self) -> ModeAccessPoint:
        """Build and return ModeAccessPoint object.

        Returns:
            ModeAccessPoint instance
        """
        # TODO: Add validation
        return self._obj
