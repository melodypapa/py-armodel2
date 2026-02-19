"""IPduMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 840)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Multiplatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.target_i_pdu_ref import (
    TargetIPduRef,
)


class IPduMapping(ARObject):
    """AUTOSAR IPduMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    introduction: Optional[DocumentationBlock]
    pdu_max_length: Optional[PositiveInteger]
    pdur_tp_chunk: Optional[PositiveInteger]
    source_i_pdu_ref: Optional[ARRef]
    target_i_pdu_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize IPduMapping."""
        super().__init__()
        self.introduction: Optional[DocumentationBlock] = None
        self.pdu_max_length: Optional[PositiveInteger] = None
        self.pdur_tp_chunk: Optional[PositiveInteger] = None
        self.source_i_pdu_ref: Optional[ARRef] = None
        self.target_i_pdu_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPduMapping":
        """Deserialize XML element to IPduMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IPduMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse introduction
        child = ARObject._find_child_element(element, "INTRODUCTION")
        if child is not None:
            introduction_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.introduction = introduction_value

        # Parse pdu_max_length
        child = ARObject._find_child_element(element, "PDU-MAX-LENGTH")
        if child is not None:
            pdu_max_length_value = child.text
            obj.pdu_max_length = pdu_max_length_value

        # Parse pdur_tp_chunk
        child = ARObject._find_child_element(element, "PDUR-TP-CHUNK")
        if child is not None:
            pdur_tp_chunk_value = child.text
            obj.pdur_tp_chunk = pdur_tp_chunk_value

        # Parse source_i_pdu_ref
        child = ARObject._find_child_element(element, "SOURCE-I-PDU")
        if child is not None:
            source_i_pdu_ref_value = ARObject._deserialize_by_tag(child, "PduTriggering")
            obj.source_i_pdu_ref = source_i_pdu_ref_value

        # Parse target_i_pdu_ref
        child = ARObject._find_child_element(element, "TARGET-I-PDU")
        if child is not None:
            target_i_pdu_ref_value = ARObject._deserialize_by_tag(child, "TargetIPduRef")
            obj.target_i_pdu_ref = target_i_pdu_ref_value

        return obj



class IPduMappingBuilder:
    """Builder for IPduMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IPduMapping = IPduMapping()

    def build(self) -> IPduMapping:
        """Build and return IPduMapping object.

        Returns:
            IPduMapping instance
        """
        # TODO: Add validation
        return self._obj
