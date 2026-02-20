"""DiagnosticComControlSpecificChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 109)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CommunicationControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cluster import (
    CommunicationCluster,
)


class DiagnosticComControlSpecificChannel(ARObject):
    """AUTOSAR DiagnosticComControlSpecificChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    specific_channel_ref: Optional[ARRef]
    specific_physical_ref: Optional[Any]
    subnet_number: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticComControlSpecificChannel."""
        super().__init__()
        self.specific_channel_ref: Optional[ARRef] = None
        self.specific_physical_ref: Optional[Any] = None
        self.subnet_number: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticComControlSpecificChannel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize specific_channel_ref
        if self.specific_channel_ref is not None:
            serialized = ARObject._serialize_item(self.specific_channel_ref, "CommunicationCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SPECIFIC-CHANNEL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize specific_physical_ref
        if self.specific_physical_ref is not None:
            serialized = ARObject._serialize_item(self.specific_physical_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SPECIFIC-PHYSICAL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize subnet_number
        if self.subnet_number is not None:
            serialized = ARObject._serialize_item(self.subnet_number, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUBNET-NUMBER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticComControlSpecificChannel":
        """Deserialize XML element to DiagnosticComControlSpecificChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticComControlSpecificChannel object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse specific_channel_ref
        child = ARObject._find_child_element(element, "SPECIFIC-CHANNEL-REF")
        if child is not None:
            specific_channel_ref_value = ARRef.deserialize(child)
            obj.specific_channel_ref = specific_channel_ref_value

        # Parse specific_physical_ref
        child = ARObject._find_child_element(element, "SPECIFIC-PHYSICAL-REF")
        if child is not None:
            specific_physical_ref_value = ARRef.deserialize(child)
            obj.specific_physical_ref = specific_physical_ref_value

        # Parse subnet_number
        child = ARObject._find_child_element(element, "SUBNET-NUMBER")
        if child is not None:
            subnet_number_value = child.text
            obj.subnet_number = subnet_number_value

        return obj



class DiagnosticComControlSpecificChannelBuilder:
    """Builder for DiagnosticComControlSpecificChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticComControlSpecificChannel = DiagnosticComControlSpecificChannel()

    def build(self) -> DiagnosticComControlSpecificChannel:
        """Build and return DiagnosticComControlSpecificChannel object.

        Returns:
            DiagnosticComControlSpecificChannel instance
        """
        # TODO: Add validation
        return self._obj
