"""PortAPIOption AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "enable_take": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # enableTake
        "error_handling": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataTransformation,
        ),  # errorHandling
        "indirect_api": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # indirectAPI
        "port": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PortPrototype,
        ),  # port
        "port_arg_values": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PortDefinedArgumentValue,
        ),  # portArgValues
        "supporteds": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SwcSupportedFeature,
        ),  # supporteds
        "transformer": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataTransformation,
        ),  # transformer
    }

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
