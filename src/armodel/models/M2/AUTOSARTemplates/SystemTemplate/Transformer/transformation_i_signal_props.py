"""TransformationISignalProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 772)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    CSTransformerErrorReactionEnum,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from abc import ABC, abstractmethod


class TransformationISignalProps(ARObject, ABC):
    """AUTOSAR TransformationISignalProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    cs_error_reaction: Optional[CSTransformerErrorReactionEnum]
    data_prototypes: list[DataPrototype]
    transformer: Optional[Any]
    def __init__(self) -> None:
        """Initialize TransformationISignalProps."""
        super().__init__()
        self.cs_error_reaction: Optional[CSTransformerErrorReactionEnum] = None
        self.data_prototypes: list[DataPrototype] = []
        self.transformer: Optional[Any] = None


class TransformationISignalPropsBuilder:
    """Builder for TransformationISignalProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransformationISignalProps = TransformationISignalProps()

    def build(self) -> TransformationISignalProps:
        """Build and return TransformationISignalProps object.

        Returns:
            TransformationISignalProps instance
        """
        # TODO: Add validation
        return self._obj
