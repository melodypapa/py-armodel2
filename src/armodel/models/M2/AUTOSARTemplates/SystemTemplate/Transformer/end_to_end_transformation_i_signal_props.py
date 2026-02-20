"""EndToEndTransformationISignalProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 808)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


@atp_variant()

class EndToEndTransformationISignalProps(ARObject):
    """AUTOSAR EndToEndTransformationISignalProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_length: Optional[PositiveInteger]
    max_data_length: Optional[PositiveInteger]
    min_data_length: Optional[PositiveInteger]
    source_id: Optional[PositiveInteger]
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
