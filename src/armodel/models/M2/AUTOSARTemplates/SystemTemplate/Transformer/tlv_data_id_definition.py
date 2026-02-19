"""TlvDataIdDefinition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 830)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.argument_data_prototype import (
    ArgumentDataPrototype,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
        AbstractImplementationDataType,
    )



class TlvDataIdDefinition(ARObject):
    """AUTOSAR TlvDataIdDefinition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    id: Optional[PositiveInteger]
    tlv_argument_ref: Optional[ARRef]
    tlv: Optional[AbstractImplementationDataType]
    tlv_record: Optional[Any]
    def __init__(self) -> None:
        """Initialize TlvDataIdDefinition."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None
        self.tlv_argument_ref: Optional[ARRef] = None
        self.tlv: Optional[AbstractImplementationDataType] = None
        self.tlv_record: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TlvDataIdDefinition":
        """Deserialize XML element to TlvDataIdDefinition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TlvDataIdDefinition object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse id
        child = ARObject._find_child_element(element, "ID")
        if child is not None:
            id_value = child.text
            obj.id = id_value

        # Parse tlv_argument_ref
        child = ARObject._find_child_element(element, "TLV-ARGUMENT")
        if child is not None:
            tlv_argument_ref_value = ARObject._deserialize_by_tag(child, "ArgumentDataPrototype")
            obj.tlv_argument_ref = tlv_argument_ref_value

        # Parse tlv
        child = ARObject._find_child_element(element, "TLV")
        if child is not None:
            tlv_value = ARObject._deserialize_by_tag(child, "AbstractImplementationDataType")
            obj.tlv = tlv_value

        # Parse tlv_record
        child = ARObject._find_child_element(element, "TLV-RECORD")
        if child is not None:
            tlv_record_value = child.text
            obj.tlv_record = tlv_record_value

        return obj



class TlvDataIdDefinitionBuilder:
    """Builder for TlvDataIdDefinition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TlvDataIdDefinition = TlvDataIdDefinition()

    def build(self) -> TlvDataIdDefinition:
        """Build and return TlvDataIdDefinition object.

        Returns:
            TlvDataIdDefinition instance
        """
        # TODO: Add validation
        return self._obj
