"""IEEE1722TpIidcConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 648)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAv.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_av_connection import (
    IEEE1722TpAvConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class IEEE1722TpIidcConnection(IEEE1722TpAvConnection):
    """AUTOSAR IEEE1722TpIidcConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    iidc_channel: Optional[PositiveInteger]
    iidc_data_block: Optional[PositiveInteger]
    iidc_fraction: Optional[PositiveInteger]
    iidc_source: Optional[Boolean]
    iidc_stream: Optional[PositiveInteger]
    iidc_sy: Optional[PositiveInteger]
    iidc_tag: Optional[PositiveInteger]
    iidc_t_code: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize IEEE1722TpIidcConnection."""
        super().__init__()
        self.iidc_channel: Optional[PositiveInteger] = None
        self.iidc_data_block: Optional[PositiveInteger] = None
        self.iidc_fraction: Optional[PositiveInteger] = None
        self.iidc_source: Optional[Boolean] = None
        self.iidc_stream: Optional[PositiveInteger] = None
        self.iidc_sy: Optional[PositiveInteger] = None
        self.iidc_tag: Optional[PositiveInteger] = None
        self.iidc_t_code: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpIidcConnection":
        """Deserialize XML element to IEEE1722TpIidcConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpIidcConnection object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse iidc_channel
        child = ARObject._find_child_element(element, "IIDC-CHANNEL")
        if child is not None:
            iidc_channel_value = child.text
            obj.iidc_channel = iidc_channel_value

        # Parse iidc_data_block
        child = ARObject._find_child_element(element, "IIDC-DATA-BLOCK")
        if child is not None:
            iidc_data_block_value = child.text
            obj.iidc_data_block = iidc_data_block_value

        # Parse iidc_fraction
        child = ARObject._find_child_element(element, "IIDC-FRACTION")
        if child is not None:
            iidc_fraction_value = child.text
            obj.iidc_fraction = iidc_fraction_value

        # Parse iidc_source
        child = ARObject._find_child_element(element, "IIDC-SOURCE")
        if child is not None:
            iidc_source_value = child.text
            obj.iidc_source = iidc_source_value

        # Parse iidc_stream
        child = ARObject._find_child_element(element, "IIDC-STREAM")
        if child is not None:
            iidc_stream_value = child.text
            obj.iidc_stream = iidc_stream_value

        # Parse iidc_sy
        child = ARObject._find_child_element(element, "IIDC-SY")
        if child is not None:
            iidc_sy_value = child.text
            obj.iidc_sy = iidc_sy_value

        # Parse iidc_tag
        child = ARObject._find_child_element(element, "IIDC-TAG")
        if child is not None:
            iidc_tag_value = child.text
            obj.iidc_tag = iidc_tag_value

        # Parse iidc_t_code
        child = ARObject._find_child_element(element, "IIDC-T-CODE")
        if child is not None:
            iidc_t_code_value = child.text
            obj.iidc_t_code = iidc_t_code_value

        return obj



class IEEE1722TpIidcConnectionBuilder:
    """Builder for IEEE1722TpIidcConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpIidcConnection = IEEE1722TpIidcConnection()

    def build(self) -> IEEE1722TpIidcConnection:
        """Build and return IEEE1722TpIidcConnection object.

        Returns:
            IEEE1722TpIidcConnection instance
        """
        # TODO: Add validation
        return self._obj
