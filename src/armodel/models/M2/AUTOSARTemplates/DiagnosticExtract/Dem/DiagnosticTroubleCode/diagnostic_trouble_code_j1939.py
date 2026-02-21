"""DiagnosticTroubleCodeJ1939 AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 221)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import (
    DiagnosticTroubleCode,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_node import (
    DiagnosticJ1939Node,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_spn import (
    DiagnosticJ1939Spn,
)


class DiagnosticTroubleCodeJ1939(DiagnosticTroubleCode):
    """AUTOSAR DiagnosticTroubleCodeJ1939."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dtc_props_props_ref: Optional[ARRef]
    fmi: Optional[PositiveInteger]
    kind: Optional[DiagnosticTroubleCode]
    node_ref: Optional[ARRef]
    spn_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeJ1939."""
        super().__init__()
        self.dtc_props_props_ref: Optional[ARRef] = None
        self.fmi: Optional[PositiveInteger] = None
        self.kind: Optional[DiagnosticTroubleCode] = None
        self.node_ref: Optional[ARRef] = None
        self.spn_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticTroubleCodeJ1939 to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticTroubleCodeJ1939, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dtc_props_props_ref
        if self.dtc_props_props_ref is not None:
            serialized = SerializationHelper.serialize_item(self.dtc_props_props_ref, "DiagnosticTroubleCode")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DTC-PROPS-PROPS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize fmi
        if self.fmi is not None:
            serialized = SerializationHelper.serialize_item(self.fmi, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FMI")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize kind
        if self.kind is not None:
            serialized = SerializationHelper.serialize_item(self.kind, "DiagnosticTroubleCode")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KIND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize node_ref
        if self.node_ref is not None:
            serialized = SerializationHelper.serialize_item(self.node_ref, "DiagnosticJ1939Node")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize spn_ref
        if self.spn_ref is not None:
            serialized = SerializationHelper.serialize_item(self.spn_ref, "DiagnosticJ1939Spn")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SPN-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTroubleCodeJ1939":
        """Deserialize XML element to DiagnosticTroubleCodeJ1939 object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticTroubleCodeJ1939 object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticTroubleCodeJ1939, cls).deserialize(element)

        # Parse dtc_props_props_ref
        child = SerializationHelper.find_child_element(element, "DTC-PROPS-PROPS-REF")
        if child is not None:
            dtc_props_props_ref_value = ARRef.deserialize(child)
            obj.dtc_props_props_ref = dtc_props_props_ref_value

        # Parse fmi
        child = SerializationHelper.find_child_element(element, "FMI")
        if child is not None:
            fmi_value = child.text
            obj.fmi = fmi_value

        # Parse kind
        child = SerializationHelper.find_child_element(element, "KIND")
        if child is not None:
            kind_value = SerializationHelper.deserialize_by_tag(child, "DiagnosticTroubleCode")
            obj.kind = kind_value

        # Parse node_ref
        child = SerializationHelper.find_child_element(element, "NODE-REF")
        if child is not None:
            node_ref_value = ARRef.deserialize(child)
            obj.node_ref = node_ref_value

        # Parse spn_ref
        child = SerializationHelper.find_child_element(element, "SPN-REF")
        if child is not None:
            spn_ref_value = ARRef.deserialize(child)
            obj.spn_ref = spn_ref_value

        return obj



class DiagnosticTroubleCodeJ1939Builder:
    """Builder for DiagnosticTroubleCodeJ1939."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTroubleCodeJ1939 = DiagnosticTroubleCodeJ1939()

    def build(self) -> DiagnosticTroubleCodeJ1939:
        """Build and return DiagnosticTroubleCodeJ1939 object.

        Returns:
            DiagnosticTroubleCodeJ1939 instance
        """
        # TODO: Add validation
        return self._obj
