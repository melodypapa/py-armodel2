"""BswSynchronousServerCallPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 79)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_call_point import (
    BswModuleCallPoint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_client_server_entry import (
    BswModuleClientServerEntry,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area_nesting_order import (
    ExclusiveAreaNestingOrder,
)


class BswSynchronousServerCallPoint(BswModuleCallPoint):
    """AUTOSAR BswSynchronousServerCallPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    called_entry_entry_ref: Optional[ARRef]
    called_from_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize BswSynchronousServerCallPoint."""
        super().__init__()
        self.called_entry_entry_ref: Optional[ARRef] = None
        self.called_from_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize BswSynchronousServerCallPoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswSynchronousServerCallPoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize called_entry_entry_ref
        if self.called_entry_entry_ref is not None:
            serialized = ARObject._serialize_item(self.called_entry_entry_ref, "BswModuleClientServerEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CALLED-ENTRY-ENTRY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize called_from_ref
        if self.called_from_ref is not None:
            serialized = ARObject._serialize_item(self.called_from_ref, "ExclusiveAreaNestingOrder")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CALLED-FROM-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswSynchronousServerCallPoint":
        """Deserialize XML element to BswSynchronousServerCallPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswSynchronousServerCallPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswSynchronousServerCallPoint, cls).deserialize(element)

        # Parse called_entry_entry_ref
        child = ARObject._find_child_element(element, "CALLED-ENTRY-ENTRY-REF")
        if child is not None:
            called_entry_entry_ref_value = ARRef.deserialize(child)
            obj.called_entry_entry_ref = called_entry_entry_ref_value

        # Parse called_from_ref
        child = ARObject._find_child_element(element, "CALLED-FROM-REF")
        if child is not None:
            called_from_ref_value = ARRef.deserialize(child)
            obj.called_from_ref = called_from_ref_value

        return obj



class BswSynchronousServerCallPointBuilder:
    """Builder for BswSynchronousServerCallPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswSynchronousServerCallPoint = BswSynchronousServerCallPoint()

    def build(self) -> BswSynchronousServerCallPoint:
        """Build and return BswSynchronousServerCallPoint object.

        Returns:
            BswSynchronousServerCallPoint instance
        """
        # TODO: Add validation
        return self._obj
