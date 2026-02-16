"""DataPrototypeTransformationProps AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_props import (
    TransformationProps,
)


class DataPrototypeTransformationProps(ARObject):
    """AUTOSAR DataPrototypeTransformationProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data_prototype_in": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataPrototype,
        ),  # dataPrototypeIn
        "network": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwDataDefProps,
        ),  # network
        "transformation_props": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TransformationProps,
        ),  # transformationProps
    }

    def __init__(self) -> None:
        """Initialize DataPrototypeTransformationProps."""
        super().__init__()
        self.data_prototype_in: Optional[DataPrototype] = None
        self.network: Optional[SwDataDefProps] = None
        self.transformation_props: Optional[TransformationProps] = None


class DataPrototypeTransformationPropsBuilder:
    """Builder for DataPrototypeTransformationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeTransformationProps = DataPrototypeTransformationProps()

    def build(self) -> DataPrototypeTransformationProps:
        """Build and return DataPrototypeTransformationProps object.

        Returns:
            DataPrototypeTransformationProps instance
        """
        # TODO: Add validation
        return self._obj
