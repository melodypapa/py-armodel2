"""ISignalIPduGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 316)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 350)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu import (
    ISignalIPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.nm_pdu import (
    NmPdu,
)


class ISignalIPduGroup(FibexElement):
    """AUTOSAR ISignalIPduGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    communication: Optional[String]
    contained_refs: list[ARRef]
    i_signal_i_pdus: list[ISignalIPdu]
    nm_pdus: list[NmPdu]
    def __init__(self) -> None:
        """Initialize ISignalIPduGroup."""
        super().__init__()
        self.communication: Optional[String] = None
        self.contained_refs: list[ARRef] = []
        self.i_signal_i_pdus: list[ISignalIPdu] = []
        self.nm_pdus: list[NmPdu] = []

    def serialize(self) -> ET.Element:
        """Serialize ISignalIPduGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ISignalIPduGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize communication
        if self.communication is not None:
            serialized = ARObject._serialize_item(self.communication, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMUNICATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize contained_refs (list to container "CONTAINED-REFS")
        if self.contained_refs:
            wrapper = ET.Element("CONTAINED-REFS")
            for item in self.contained_refs:
                serialized = ARObject._serialize_item(item, "ISignalIPduGroup")
                if serialized is not None:
                    child_elem = ET.Element("CONTAINED-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize i_signal_i_pdus (list to container "I-SIGNAL-I-PDUS")
        if self.i_signal_i_pdus:
            wrapper = ET.Element("I-SIGNAL-I-PDUS")
            for item in self.i_signal_i_pdus:
                serialized = ARObject._serialize_item(item, "ISignalIPdu")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize nm_pdus (list to container "NM-PDUS")
        if self.nm_pdus:
            wrapper = ET.Element("NM-PDUS")
            for item in self.nm_pdus:
                serialized = ARObject._serialize_item(item, "NmPdu")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignalIPduGroup":
        """Deserialize XML element to ISignalIPduGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ISignalIPduGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ISignalIPduGroup, cls).deserialize(element)

        # Parse communication
        child = ARObject._find_child_element(element, "COMMUNICATION")
        if child is not None:
            communication_value = child.text
            obj.communication = communication_value

        # Parse contained_refs (list from container "CONTAINED-REFS")
        obj.contained_refs = []
        container = ARObject._find_child_element(element, "CONTAINED-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.contained_refs.append(child_value)

        # Parse i_signal_i_pdus (list from container "I-SIGNAL-I-PDUS")
        obj.i_signal_i_pdus = []
        container = ARObject._find_child_element(element, "I-SIGNAL-I-PDUS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.i_signal_i_pdus.append(child_value)

        # Parse nm_pdus (list from container "NM-PDUS")
        obj.nm_pdus = []
        container = ARObject._find_child_element(element, "NM-PDUS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.nm_pdus.append(child_value)

        return obj



class ISignalIPduGroupBuilder:
    """Builder for ISignalIPduGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalIPduGroup = ISignalIPduGroup()

    def build(self) -> ISignalIPduGroup:
        """Build and return ISignalIPduGroup object.

        Returns:
            ISignalIPduGroup instance
        """
        # TODO: Add validation
        return self._obj
