"""PortAPIOption AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 589)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2045)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_PortAPIOptions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
    DataTransformation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.port_defined_argument_value import (
    PortDefinedArgumentValue,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.swc_supported_feature import (
    SwcSupportedFeature,
)


class PortAPIOption(ARObject):
    """AUTOSAR PortAPIOption."""

    enable_take: Optional[Boolean]
    error_handling: Optional[DataTransformation]
    indirect_api: Optional[Boolean]
    port: Optional[PortPrototype]
    port_arg_values: list[PortDefinedArgumentValue]
    supporteds: list[SwcSupportedFeature]
    transformer: Optional[DataTransformation]
    def __init__(self) -> None:
        """Initialize PortAPIOption."""
        super().__init__()
        self.enable_take: Optional[Boolean] = None
        self.error_handling: Optional[DataTransformation] = None
        self.indirect_api: Optional[Boolean] = None
        self.port: Optional[PortPrototype] = None
        self.port_arg_values: list[PortDefinedArgumentValue] = []
        self.supporteds: list[SwcSupportedFeature] = []
        self.transformer: Optional[DataTransformation] = None


class PortAPIOptionBuilder:
    """Builder for PortAPIOption."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortAPIOption = PortAPIOption()

    def build(self) -> PortAPIOption:
        """Build and return PortAPIOption object.

        Returns:
            PortAPIOption instance
        """
        # TODO: Add validation
        return self._obj
