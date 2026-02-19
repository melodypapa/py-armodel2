"""McParameterElementGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 181)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class McParameterElementGroup(ARObject):
    """AUTOSAR McParameterElementGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ram_location_ref: Optional[ARRef]
    rom_location_ref: Optional[ARRef]
    short_label: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize McParameterElementGroup."""
        super().__init__()
        self.ram_location_ref: Optional[ARRef] = None
        self.rom_location_ref: Optional[ARRef] = None
        self.short_label: Optional[Identifier] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "McParameterElementGroup":
        """Deserialize XML element to McParameterElementGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized McParameterElementGroup object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ram_location_ref
        child = ARObject._find_child_element(element, "RAM-LOCATION")
        if child is not None:
            ram_location_ref_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.ram_location_ref = ram_location_ref_value

        # Parse rom_location_ref
        child = ARObject._find_child_element(element, "ROM-LOCATION")
        if child is not None:
            rom_location_ref_value = ARObject._deserialize_by_tag(child, "ParameterDataPrototype")
            obj.rom_location_ref = rom_location_ref_value

        # Parse short_label
        child = ARObject._find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = child.text
            obj.short_label = short_label_value

        return obj



class McParameterElementGroupBuilder:
    """Builder for McParameterElementGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: McParameterElementGroup = McParameterElementGroup()

    def build(self) -> McParameterElementGroup:
        """Build and return McParameterElementGroup object.

        Returns:
            McParameterElementGroup instance
        """
        # TODO: Add validation
        return self._obj
