"""BswModuleClientServerEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 53)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)


class BswModuleClientServerEntry(Referrable):
    """AUTOSAR BswModuleClientServerEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    encapsulated_ref: Optional[ARRef]
    is_reentrant: Optional[Boolean]
    is_synchronous: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize BswModuleClientServerEntry."""
        super().__init__()
        self.encapsulated_ref: Optional[ARRef] = None
        self.is_reentrant: Optional[Boolean] = None
        self.is_synchronous: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize BswModuleClientServerEntry to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswModuleClientServerEntry, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize encapsulated_ref
        if self.encapsulated_ref is not None:
            serialized = ARObject._serialize_item(self.encapsulated_ref, "BswModuleEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENCAPSULATED-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_reentrant
        if self.is_reentrant is not None:
            serialized = ARObject._serialize_item(self.is_reentrant, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-REENTRANT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_synchronous
        if self.is_synchronous is not None:
            serialized = ARObject._serialize_item(self.is_synchronous, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-SYNCHRONOUS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModuleClientServerEntry":
        """Deserialize XML element to BswModuleClientServerEntry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswModuleClientServerEntry object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswModuleClientServerEntry, cls).deserialize(element)

        # Parse encapsulated_ref
        child = ARObject._find_child_element(element, "ENCAPSULATED-REF")
        if child is not None:
            encapsulated_ref_value = ARRef.deserialize(child)
            obj.encapsulated_ref = encapsulated_ref_value

        # Parse is_reentrant
        child = ARObject._find_child_element(element, "IS-REENTRANT")
        if child is not None:
            is_reentrant_value = child.text
            obj.is_reentrant = is_reentrant_value

        # Parse is_synchronous
        child = ARObject._find_child_element(element, "IS-SYNCHRONOUS")
        if child is not None:
            is_synchronous_value = child.text
            obj.is_synchronous = is_synchronous_value

        return obj



class BswModuleClientServerEntryBuilder:
    """Builder for BswModuleClientServerEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModuleClientServerEntry = BswModuleClientServerEntry()

    def build(self) -> BswModuleClientServerEntry:
        """Build and return BswModuleClientServerEntry object.

        Returns:
            BswModuleClientServerEntry instance
        """
        # TODO: Add validation
        return self._obj
