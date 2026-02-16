"""SOMEIPTransformationISignalProps AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.tlv_data_id_definition_set import (
    TlvDataIdDefinitionSet,
)


class SOMEIPTransformationISignalProps(ARObject):
    """AUTOSAR SOMEIPTransformationISignalProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "implements": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # implements
        "interface_version": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # interfaceVersion
        "is_dynamic": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # isDynamic
        "message_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SOMEIPMessageTypeEnum,
        ),  # messageType
        "size_of_array": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # sizeOfArray
        "size_of_string": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # sizeOfString
        "size_of_struct": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # sizeOfStruct
        "size_of_union": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # sizeOfUnion
        "tlv_data_ids": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=TlvDataIdDefinitionSet,
        ),  # tlvDataIds
    }

    def __init__(self) -> None:
        """Initialize SOMEIPTransformationISignalProps."""
        super().__init__()
        self.implements: Optional[Boolean] = None
        self.interface_version: Optional[PositiveInteger] = None
        self.is_dynamic: Optional[Boolean] = None
        self.message_type: Optional[SOMEIPMessageTypeEnum] = None
        self.size_of_array: Optional[PositiveInteger] = None
        self.size_of_string: Optional[PositiveInteger] = None
        self.size_of_struct: Optional[PositiveInteger] = None
        self.size_of_union: Optional[PositiveInteger] = None
        self.tlv_data_ids: list[TlvDataIdDefinitionSet] = []


class SOMEIPTransformationISignalPropsBuilder:
    """Builder for SOMEIPTransformationISignalProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SOMEIPTransformationISignalProps = SOMEIPTransformationISignalProps()

    def build(self) -> SOMEIPTransformationISignalProps:
        """Build and return SOMEIPTransformationISignalProps object.

        Returns:
            SOMEIPTransformationISignalProps instance
        """
        # TODO: Add validation
        return self._obj
