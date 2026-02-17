"""EndToEndTransformationISignalProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 808)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class EndToEndTransformationISignalProps(ARObject):
    """AUTOSAR EndToEndTransformationISignalProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data_length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # dataLength
        "max_data_length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxDataLength
        "min_data_length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minDataLength
        "source_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # sourceId
    }

    def __init__(self) -> None:
        """Initialize EndToEndTransformationISignalProps."""
        super().__init__()
        self.data_length: Optional[PositiveInteger] = None
        self.max_data_length: Optional[PositiveInteger] = None
        self.min_data_length: Optional[PositiveInteger] = None
        self.source_id: Optional[PositiveInteger] = None


class EndToEndTransformationISignalPropsBuilder:
    """Builder for EndToEndTransformationISignalProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndTransformationISignalProps = EndToEndTransformationISignalProps()

    def build(self) -> EndToEndTransformationISignalProps:
        """Build and return EndToEndTransformationISignalProps object.

        Returns:
            EndToEndTransformationISignalProps instance
        """
        # TODO: Add validation
        return self._obj
